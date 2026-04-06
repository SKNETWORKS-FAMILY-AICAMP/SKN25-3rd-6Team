import streamlit as st
import os
import sys
import html
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from retrieval import CardRetriever

# page setting
st.set_page_config(
    page_title="PickCardU",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS
css_path = os.path.join(os.path.dirname(__file__), "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# initialize retriever and llm
@st.cache_resource
def init_retriever():
    """CardRetriever를 한 번만 생성하여 캐싱"""
    return CardRetriever()

@st.cache_resource
def init_llm():
    """ChatOpenAI를 한 번만 생성하여 캐싱"""
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY"),
    )

retriever = init_retriever()
llm = init_llm()

# MBTI prompts loading
@st.cache_data
def load_mbti_prompts():
    """prompts.yml에서 MBTI별 프롬프트를 로드"""
    prompts_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "prompts", "prompts.yml"
    )
    with open(prompts_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

MBTI_PROMPTS = load_mbti_prompts()
MBTI_LIST = list(MBTI_PROMPTS.keys())


@st.cache_data
def load_card_list():
    """ChromaDB에 저장된 카드명 목록을 가져옴"""
    try:
        info = retriever.get_db_info()
        cards = sorted(info.get("cards", {}).keys())
        # 'Unknown' 등 무의미한 항목 제거
        return [c for c in cards if c and c != "Unknown"]
    except Exception:
        return []

AVAILABLE_CARDS = load_card_list()


def build_rag_chain(mbti_type: str, has_registered_cards: bool = False):
    """선택된 MBTI에 맞는 RAG 체인을 생성 (보유 카드 유무에 따라 지시문 추가)"""
    template = MBTI_PROMPTS[mbti_type]["template"]

    # 보유 카드가 있을 때 추가 지시문 삽입
    if has_registered_cards:
        card_instruction = """
    [보유 카드 우선 답변 원칙]
    사용자가 보유 중인 카드 정보가 [보유 카드 정보] 섹션에 제공됩니다.
    답변 시 반드시 아래 순서를 따르십시오:
    1단계) 먼저 [보유 카드 정보]에서 질문과 관련된 혜택이 있는지 확인하고, 있다면 해당 카드의 혜택을 가장 먼저 안내하십시오.
    2단계) 보유 카드에 관련 혜택이 없거나 부족한 경우에만, [추천 카드 정보]에서 더 적합한 카드를 추천하십시오.
    3단계) 보유 카드 혜택과 추천 카드를 비교해 보여주면 사용자에게 더 유용합니다.
    - 보유 카드를 언급할 때는 "고객님이 보유하신 [카드명]의 경우..." 형태로 명확히 구분하십시오.
    - 추천 카드를 언급할 때는 "추가로 추천드리는 카드는..." 형태로 구분하십시오.
    """
        template = template.rstrip() + "\n" + card_instruction

    prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])
    return prompt | llm | StrOutputParser()


def get_rag_answer(question: str, mbti_type: str, chat_history: list = None) -> str:
    """
    보유 카드 우선 검색하고 부족하면 일반 추천 카드를 검색하여 MBTI 맞춤 LLM 답변 생성

    흐름:
    1) 등록된 카드가 있으면 해당 카드들에서 질문 관련 청크 검색
    2) 보유 카드 결과가 충분하지 않으면 일반 검색으로 추천 카드 보충
    3) 컨텍스트를 [보유 카드 정보] / [추천 카드 정보]로 구분하여 LLM에 전달
    """
    if chat_history is None:
        chat_history = []
    registered = st.session_state.get("registered_cards", [])
    has_registered = bool(registered)

    # registered 카드 검색 결과를 우선적으로 컨텍스트에 포함
    my_context = ""
    my_card_names_found = set()

    if has_registered:
        my_card_docs = []
        for card_name in registered:
            docs = retriever.search_by_metadata(question, card_name=card_name, k=3)
            my_card_docs.extend(docs)

        if my_card_docs:
            my_context_parts = []
            for doc in my_card_docs:
                name = doc.metadata.get("card_name", "")
                text = doc.page_content[:400] if doc.page_content else ""
                if text.strip():
                    my_context_parts.append(f"[{name}]\n{text}")
                    my_card_names_found.add(name)
            my_context = "\n---\n".join(my_context_parts)

    # 보유 카드에서 충분한 정보가 없으면 일반 검색으로 보충
    general_results = retriever.search_with_score(question, k=5)

    # 보유 카드에서 이미 다룬 카드는 스킵하면서 추천 카드 컨텍스트 생성
    recommend_parts = []
    for doc, score in general_results:
        card = doc.metadata.get("card_name", "")
        if card in my_card_names_found:
            continue
        text = doc.page_content[:400] if doc.page_content else ""
        if text.strip():
            recommend_parts.append(f"[{card}] (유사도: {score:.4f})\n{text}")

    recommend_context = "\n---\n".join(recommend_parts) if recommend_parts else ""

    # final context assembly
    if has_registered and my_context:
        context = f"[보유 카드 정보]\n{my_context}"
        if recommend_context:
            context += f"\n\n[추천 카드 정보]\n{recommend_context}"
    elif recommend_context:
        context = f"[추천 카드 정보]\n{recommend_context}"
    else:
        return "죄송합니다. 관련 카드 정보를 찾지 못했습니다."

    # RAG chain answer generation
    chain = build_rag_chain(mbti_type, has_registered_cards=has_registered)
    answer = chain.invoke({"context": context, "question": question, "chat_history": chat_history})
    return answer

# session state setup
if "sessions" not in st.session_state:
    st.session_state.sessions = [
        {"id": 0, "title": "새 대화", "messages": []}
    ]
    st.session_state.next_session_id = 1

if "active_session_id" not in st.session_state:
    st.session_state.active_session_id = 0

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "registered_cards" not in st.session_state:
    st.session_state.registered_cards = []  # 사용자가 등록한 카드명 리스트

if "page_mode" not in st.session_state:
    st.session_state.page_mode = "chat"  # 'chat' 또는 'card_register'


def get_active_session():
    """현재 활성 세션을 반환"""
    for s in st.session_state.sessions:
        if s["id"] == st.session_state.active_session_id:
            return s
    return st.session_state.sessions[0]


def create_new_session():
    """새 대화 세션을 생성하고 활성화"""
    new_id = st.session_state.next_session_id
    st.session_state.sessions.insert(0, {
        "id": new_id,
        "title": "새 대화",
        "messages": [],
    })
    st.session_state.next_session_id = new_id + 1
    st.session_state.active_session_id = new_id

# sidebar
with st.sidebar:
    st.markdown("""
    <div class="logo-area">
        <div class="logo-text">
            <span class="logo-pick">Pick</span><span class="logo-card">Card</span><span class="logo-u">U</span>
        </div>
        <div class="logo-version">v. 1.0.0</div>
    </div>
    """, unsafe_allow_html=True)

    # MBTI selector
    st.markdown("<p style='font-size:0.8rem; color:#999; margin-bottom:0.2rem;'>나의 MBTI</p>", unsafe_allow_html=True)
    mbti_options = ["{} – {}".format(m, MBTI_PROMPTS[m]["name"]) for m in MBTI_LIST]
    selected_idx = st.selectbox(
        "MBTI 선택",
        range(len(MBTI_LIST)),
        format_func=lambda i: mbti_options[i],
        index=MBTI_LIST.index(st.session_state.selected_mbti) if st.session_state.selected_mbti else 0,
        label_visibility="collapsed",
    )
    st.session_state.selected_mbti = MBTI_LIST[selected_idx]

    st.markdown("<hr style='border:none; border-top:1px solid #eee; margin:0.8rem 0;'>", unsafe_allow_html=True)

    # 새 대화 버튼
    if st.button("➕  새 대화", key="new_chat", use_container_width=True):
        create_new_session()
        st.rerun()

    # 대화 세션 목록
    st.markdown("<p style='font-size:0.75rem; color:#aaa; margin:0.6rem 0 0.3rem 0.2rem;'>이전 대화</p>", unsafe_allow_html=True)
    with st.container(height=220, border=False):
        for session in st.session_state.sessions:
            is_active = session["id"] == st.session_state.active_session_id
            label = session["title"]
            if st.button(
                label,
                key=f"session_{session['id']}",
                use_container_width=True,
            ):
                st.session_state.active_session_id = session["id"]
                st.rerun()

    st.markdown("<hr style='border:none; border-top:1px solid #eee; margin:1rem 0 0.5rem 0;'>", unsafe_allow_html=True)

    n_cards = len(st.session_state.registered_cards)
    card_btn_label = f"💳  내 카드 관리 ({n_cards}장)" if n_cards > 0 else "💳  카드 등록"
    if st.button(card_btn_label, key="card_register_btn", use_container_width=True):
        st.session_state.page_mode = "card_register" if st.session_state.page_mode != "card_register" else "chat"
        st.rerun()

    # sidebar button styling
    st.markdown(f"""
    <style>
    div[data-testid="stSidebar"] .stButton > button {{
        border-radius: 10px;
        padding: 0.55rem 1rem;
        font-size: 0.85rem;
        font-family: 'Noto Sans KR', sans-serif;
        transition: background 0.15s;
        text-align: left !important;
        justify-content: flex-start !important;
    }}
    /* 새 대화 버튼 */
    div[data-testid="stSidebar"] .stButton:first-of-type > button {{
        background-color: #F5C842 !important;
        color: #333 !important;
        font-weight: 600 !important;
        text-align: center !important;
        justify-content: center !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# CARD REGISTER PAGE
if st.session_state.page_mode == "card_register":
    st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)
    st.markdown('<p class="card-reg-header">💳 내 카드 등록 / 관리</p>', unsafe_allow_html=True)

    # card display section
    st.markdown('<div class="registered-section">', unsafe_allow_html=True)
    st.markdown('<p class="registered-section-title">등록된 내 카드</p>', unsafe_allow_html=True)

    if st.session_state.registered_cards:
        chips_html = ""
        for card in st.session_state.registered_cards:
            chips_html += f'<span class="registered-card-chip"><span class="chip-icon">💳</span>{card}</span>'
        st.markdown(chips_html, unsafe_allow_html=True)
    else:
        st.markdown('<p class="no-cards-msg">아직 등록된 카드가 없습니다.</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
    # card add section
    st.markdown('<div class="registered-section">', unsafe_allow_html=True)
    st.markdown('<p class="registered-section-title">카드 추가</p>', unsafe_allow_html=True)

    if AVAILABLE_CARDS:
        addable = [c for c in AVAILABLE_CARDS if c not in st.session_state.registered_cards]
        if addable:
            selected_to_add = st.multiselect(
                "등록할 카드를 선택하세요",
                options=addable,
                default=[],
                placeholder="카드 이름을 검색하세요...",
                label_visibility="collapsed",
            )
            if st.button("✅ 선택한 카드 등록", key="add_cards_btn", use_container_width=True):
                if selected_to_add:
                    st.session_state.registered_cards.extend(selected_to_add)
                    st.rerun()
        else:
            st.info("모든 카드가 이미 등록되어 있습니다.")
    else:
        st.warning("데이터베이스에서 카드 목록을 불러올 수 없습니다.")

    st.markdown('</div>', unsafe_allow_html=True)

    # card remove section
    if st.session_state.registered_cards:
        st.markdown('<div class="registered-section">', unsafe_allow_html=True)
        st.markdown('<p class="registered-section-title">카드 해제</p>', unsafe_allow_html=True)

        selected_to_remove = st.multiselect(
            "해제할 카드를 선택하세요",
            options=st.session_state.registered_cards,
            default=[],
            placeholder="해제할 카드를 선택...",
            label_visibility="collapsed",
        )
        if st.button("🗑️ 선택한 카드 해제", key="remove_cards_btn", use_container_width=True):
            if selected_to_remove:
                st.session_state.registered_cards = [
                    c for c in st.session_state.registered_cards if c not in selected_to_remove
                ]
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💬 대화로 돌아가기", key="back_to_chat", use_container_width=True):
        st.session_state.page_mode = "chat"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# chat page
else:
    active_session = get_active_session()

    # messages display
    chat_html = '<div class="chat-wrapper">'
    for msg in active_session["messages"]:
        content = html.escape(msg["content"]).replace("\n", "<br>")
        if msg["role"] == "user":
            chat_html += (
                '<div class="msg-user-row">'
                f'<div class="msg-user-bubble">{content}</div>'
                '<div class="avatar">👤</div>'
                '</div>'
            )
        else:
            chat_html += (
                '<div class="msg-bot-row">'
                '<div class="avatar">🤖</div>'
                f'<div class="msg-bot-bubble">{content}</div>'
                '</div>'
            )
    chat_html += '<div class="scroll-spacer"></div></div>'
    st.markdown(chat_html, unsafe_allow_html=True)

    user_input = st.chat_input("궁금한 점이 있다면 입력하세요.")

    if user_input and user_input.strip():
        session = get_active_session()

        # session title setting
        if len(session["messages"]) == 0:
            session["title"] = user_input[:25] + ("..." if len(user_input) > 25 else "")

        # display user message immediately
        escaped_input = html.escape(user_input).replace("\n", "<br>")
        st.markdown(
            '<div class="msg-user-row">'
            f'<div class="msg-user-bubble">{escaped_input}</div>'
            '<div class="avatar">👤</div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # bot placeholder
        bot_placeholder = st.empty()
        bot_placeholder.markdown(
            '<div class="msg-bot-row">'
            '<div class="avatar">🤖</div>'
            '<div class="msg-bot-bubble">⏳ 카드 혜택을 검색하고 있습니다...</div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # RAG response generation
        mbti = st.session_state.selected_mbti or MBTI_LIST[0]
        history_messages = []
        for m in session["messages"]:
            if m["role"] == "user":
                history_messages.append(HumanMessage(content=m["content"]))
            else:
                history_messages.append(AIMessage(content=m["content"]))
        try:
            bot_reply = get_rag_answer(user_input, mbti_type=mbti, chat_history=history_messages)
        except Exception as e:
            bot_reply = f"죄송합니다. 답변 생성 중 오류가 발생했습니다: {e}"

        # update bot response
        escaped_reply = html.escape(bot_reply).replace("\n", "<br>")
        bot_placeholder.markdown(
            '<div class="msg-bot-row">'
            '<div class="avatar">🤖</div>'
            f'<div class="msg-bot-bubble">{escaped_reply}</div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # message history update
        session["messages"].append({"role": "user", "content": user_input})
        session["messages"].append({"role": "assistant", "content": bot_reply})
        st.rerun()