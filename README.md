# PickCardU
### MBTI 기반 개인 맞춤형 신용카드 큐레이션 RAG 챗봇

<br>

## 프로젝트 소개

> **"내 소비 패턴에 딱 맞는 카드, AI가 MBTI 말투로 추천해드립니다"**

신용카드 시장의 카드 수가 폭발적으로 증가하면서 소비자들이 자신에게 맞는 카드를 선택하기 어려운 환경이 되었습니다.
카드사별 혜택 구조가 복잡하고 다양하여 단순 비교가 어렵고, 개인의 소비 패턴과 성향에 맞는 맞춤형 카드 추천 서비스가 부재한 상황입니다.

**PickCardU**는 RAG(Retrieval-Augmented Generation) 기술로 카드 약관을 정확히 검색하고,
사용자의 MBTI 유형에 맞는 말투로 카드를 추천·설명해주는 개인 맞춤형 챗봇입니다.

<br>

## 프로젝트 기간

**2026.04.01 ~ 2026.04.07** (SK Networks AI Camp 25기 · 6팀 · 3차 미니 프로젝트)

<br>

## 팀원 소개

<table>
  <tr>
    <td align="center"><img src="assets/yeonypark.png" width="100"/></td>
    <td align="center"><img src="assets/seohyunkim.png" width="100"/></td>
    <td align="center"><img src="assets/jihyunpark.png" width="100"/></td>
    <td align="center"><img src="assets/moonsusin.png" width="100"/></td>
    <td align="center"><img src="assets/geunhyuklee.png" width="100"/></td>
  </tr>
  <tr>
    <td align="center"><b>박연정</b><br>(오 박사)</td>
    <td align="center"><b>김서현</b><br>(이상해씨)</td>
    <td align="center"><b>박지현</b><br>(망나뇽)</td>
    <td align="center"><b>신문수</b><br>(삐딱구리)</td>
    <td align="center"><b>이근혁</b><br>(고라파덕)</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/yeony-park">@yeony-park</a></td>
    <td align="center"><a href="https://github.com/bizseohyunkim">@bizseohyunkim</a></td>
    <td align="center"><a href="https://github.com/qkrwlgus89">@qkrwlgus89</a></td>
    <td align="center"><a href="https://github.com/anstn3375">@anstn3375</a></td>
    <td align="center"><a href="https://github.com/keunlee726">@keunlee726</a></td>
  </tr>
  <tr>
    <td align="center">팀장 · 테크 리딩<br>데이터수집(신한, IBK)<br>MBTI 프롬프트(INFP)<br>Docker 환경세팅 · UI/UX</td>
    <td align="center">데이터수집(삼성, 하나)<br>MBTI 프롬프트(INTP)<br>임베딩 & 벡터DB 저장<br>PPT 제작</td>
    <td align="center">데이터수집(현대, 국민)<br>프롬프트 엔지니어링<br>PPT 제작 · 발표</td>
    <td align="center">데이터수집(NH, BC)<br>MBTI 프롬프트(ISFJ)<br>PDF OCR<br>데이터 로드/청킹</td>
    <td align="center">데이터수집(우리, 롯데)<br>MBTI 프롬프트(INTJ)<br>프롬프트 테스트/개선<br>SQLite DB · 발표</td>
  </tr>
</table>

<br>

## 기술 스택

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

### Database / Infra
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

### Tools
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

<br>

## 주제 선정 배경

- 하루에 1.4장씩 단종되는 카드 시장 → 소비자가 최신 혜택을 일일이 파악하기 어려움
- 카드사별 혜택 구조가 복잡하고 다양하여 단순 비교가 어려움
- 개인의 소비 패턴과 성향에 맞는 맞춤형 카드 추천 서비스 부재

**→ RAG 기반 LLM으로 hallucination 없이 실제 카드 데이터에 기반한 신뢰성 높은 큐레이션 서비스 구현**  
**→ MBTI 성향별 맞춤 프롬프트로 사용자 친화적인 개인화 응답 제공**

<br>

## 주요 기능

| 기능 | 설명 |
|------|------|
| 카드 추천 | 사용자 질문 + 보유 카드 기반 맞춤 카드 추천 |
| MBTI 말투 | 16가지 MBTI 페르소나로 개인화된 답변 제공 |
| 카드 등록 | 보유 카드 등록 후 혜택 비교 가능 |
| 카드 Q&A | 카드 약관 기반 정확한 혜택 질의응답 (RAG) |
| 대화 이력 | 사용자별 채팅 히스토리 저장 |

<br>

## 시스템 아키텍처

```
데이터 파이프라인                         RAG 파이프라인
──────────────────────                   ──────────────────────
카드 PDF 수집 (10개 카드사)    ──►        사용자 질문 (MBTI + 질의)
         ↓                                        ↓
   전처리 / OCR                              RAG 검색 (유사도)
   (PyPDF, EasyOCR)                               ↓
         ↓                                   GPT LLM
       청킹                              (MBTI 프롬프트 적용)
  (LangChain TextSplitter)                        ↓
         ↓                                  SQLite 저장
       임베딩                           (사용자 / 대화 이력)
  (text-embedding-3-small)                        ↓
         ↓                              Streamlit UI 답변 출력
  ChromaDB 저장  ──────────────────────►
```

<br>

## 데이터 파이프라인

**10개 카드사 공식 홈페이지**에서 카드 상품 설명서 PDF를 수집하여 처리합니다.

| 단계 | 도구 | 설명 |
|------|------|------|
| PDF 수집 | - | 삼성, 하나, BC, 신한, 현대, 국민, NH, 우리, 롯데, IBK |
| 전처리/OCR | PyPDF, EasyOCR | 텍스트 추출 및 정제 |
| 청킹 | LangChain TextSplitter | chunk_size=800, overlap=120 |
| 임베딩 | OpenAI text-embedding-3-small | 벡터 변환 |
| 벡터 저장 | ChromaDB PersistentClient | 유사도 검색 |

<br>

## 핵심 기능 구현

### 임베딩 & ChromaDB
- `text-embedding-3-small` 모델로 벡터 변환 및 저장
- LangChain 연동, PersistentClient 사용
- 유사도 기반 검색

### RAG 검색 전략
- 유사도 검색 (similarity)
- 카드명 그룹화 및 키워드 필터링
- 배치 검색 + LRU 캐시 적용

### MBTI 기반 프롬프트 엔지니어링
- 16가지 MBTI 페르소나 개인화 답변 스타일
- Hallucination 방지 (context 내 정보만 사용)
- GPT-4o 연동

<br>

## 시퀀스 다이어그램

```mermaid
sequenceDiagram
    autonumber
    participant U as 사용자
    participant F as Streamlit (App)
    participant DB as SQLite (RDB)
    participant R as RAG Chain (LangChain)
    participant V as ChromaDB (Vector DB)

    Note over U,F: 최초 진입 — 로그인
    U->>F: 이름 + MBTI 입력
    F->>DB: get_or_create_user(name, mbti)
    DB-->>F: User {user_id, mbti}
    F->>DB: get_user_cards(user_id) / get_chat_history(user_id)
    DB-->>F: {registered_cards, chat_history}
    F-->>U: 채팅 화면 진입

    Note over U,V: 질문 처리
    U->>F: "스타벅스 할인 카드 알려줘"
    F->>R: 질문 + MBTI + 보유 카드 목록 전달

    alt 보유 카드 있음
        R->>V: search_by_metadata(question, card_name)
        V-->>R: 보유 카드 관련 청크 반환
    end

    alt 보유 카드 없거나 결과 부족
        R->>V: search_with_score(question, k=5)
        V-->>R: 유사도 상위 청크 반환
    end

    R->>R: [LLM] MBTI 페르소나 + RAG Rules 적용하여 답변 생성
    R-->>F: 최종 답변

    F->>DB: save_chat_message(user_id, "user", question)
    F->>DB: save_chat_message(user_id, "assistant", answer)
    F-->>U: 텍스트 답변 표시
```

<br>

## ERD

```mermaid
erDiagram
    USERS ||--o{ USER_CARDS : "owns"
    USERS ||--o{ CHAT_HISTORY : "has"

    USERS {
        int user_id PK "Primary Key"
        string username "사용자 이름"
        string mbti "MBTI"
        datetime created_at "가입일"
    }

    USER_CARDS {
        int card_id PK "Primary Key"
        int user_id FK "사용자 참조"
        string card_name "보유 카드 명칭"
        string company "카드사"
    }

    CHAT_HISTORY {
        int chat_id PK "Primary Key"
        int user_id FK "사용자 참조"
        string role "user 또는 assistant"
        text content "대화 내용"
        datetime created_at "메시지 생성 시간"
    }
```

<br>

## 프로젝트 구조

```
SKN25-3rd-6Team/
├── app.py                  # Streamlit 메인 앱
├── docker-compose.yml      # Docker 설정
├── Dockerfile
├── requirements.txt
├── .env                    # 환경변수 (git 제외)
├── .gitignore
│
├── src/                    # 핵심 모듈
│   ├── data_loader.py      # PDF 문서 로딩
│   ├── chunking.py         # 텍스트 청킹
│   ├── embedding.py        # 임베딩 & ChromaDB 저장
│   ├── Easyocr.py          # EasyOCR 처리
│   ├── ocr.py              # GPT Vision OCR
│   ├── retrieval.py        # 검색 전략
│   ├── templates.py        # 프롬프트 템플릿
│   └── db/                 # SQLite CRUD
│       ├── __init__.py
│       ├── crud.py
│       ├── database.py
│       ├── init_db.py
│       └── models.py
│
├── data/
│   ├── clean_data/         # 전처리된 PDF
│   ├── raw/                # 원본 PDF
│   └── ocr_output/         # OCR 결과 txt
│
├── chroma_db/              # 벡터 DB 저장소
├── sqlite_db/              # SQLite DB 저장소
├── prompts/
│   ├── prompts.yml         # MBTI 프롬프트
│   └── rag_rules.yml       # RAG 규칙
└── assets/                 # 이미지 등 정적 파일
```

<br>

## 실행 방법

### 환경변수 설정

`.env` 파일을 루트에 생성하고 아래 내용을 입력하세요:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

### Docker로 실행 (권장)

```bash
# 1. 레포지토리 클론
git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN25-3rd-6Team.git
cd SKN25-3rd-6Team

# 2. 이미지 빌드 및 컨테이너 실행
docker-compose up --build -d

# 3. 실행 확인
docker-compose ps

# 4. 컨테이너 내부 진입 (선택)
docker-compose exec app bash

# 5. 브라우저에서 http://localhost:8501 접속
```

> `/data`, `/src`, `/chroma_db`, `/sqlite_db` 디렉토리는 마운트되어 있어 로컬과 공유됩니다.

---

### 로컬에서 실행

```bash
# 1. 레포지토리 클론
git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN25-3rd-6Team.git
cd SKN25-3rd-6Team

# 2. 가상환경 생성 및 활성화
python -m venv .venv

# Windows
.\.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. Streamlit 실행
streamlit run app.py
```

<br>

## src 모듈 설명

| 파일 | 설명 |
|------|------|
| `data_loader.py` | `clean_data` 폴더의 PDF를 파일 단위 Document로 로딩 |
| `chunking.py` | RecursiveCharacterTextSplitter로 텍스트 청킹 (chunk_size=800, overlap=120) |
| `embedding.py` | OpenAI `text-embedding-3-small`로 임베딩 후 ChromaDB 저장 |
| `Easyocr.py` | EasyOCR로 이미지형 PDF 텍스트 추출 및 txt 저장 |
| `ocr.py` | GPT-4 Vision API로 PDF 페이지 OCR |
| `retrieval.py` | 보유 카드 메타데이터 필터링 + 유사도 fallback 검색 |
| `templates.py` | MBTI별 시스템 프롬프트 + RAG 규칙 체인 구성 |

<br>

## 커밋 컨벤션

| Type | 설명 | 예시 |
|------|------|------|
| `feat` | 새 기능 추가 | `feat: 로그인 UI 추가` |
| `fix` | 버그 수정 | `fix: 중복 체크 오류 수정` |
| `docs` | 문서 변경 | `docs: README 설치 방법 보강` |
| `style` | 포맷/스타일 | `style: lint 규칙에 맞춰 정리` |
| `refactor` | 구조 개선 | `refactor: 회원가입 로직 분리` |
| `test` | 테스트 관련 | `test: signup API 테스트 추가` |
| `chore` | 환경/설정 | `chore: deps 업데이트` |

<br>

## Git 브랜치 전략

```bash
# 1. main 최신 상태 받아오기
git checkout main
git pull origin main

# 2. 내 브랜치로 이동
git checkout 브랜치명

# 3. main 내용을 내 브랜치에 반영 (충돌 방지)
git merge main

# 4. 작업 후 커밋
git add .
git commit -m "feat: 기능 설명"

# 5. 내 브랜치 푸시
git push origin 브랜치명
```

<br>

## 회고

> **박연정** — 팀원 각자가 카드사 데이터를 수집하고 전처리하는 과정에서 실제 금융 데이터의 복잡성을 체감했습니다. RAG 파이프라인을 직접 구축하며 단순 LLM 활용을 넘어 hallucination을 줄이는 것이 얼마나 중요한지 깨달았습니다. 16가지 MBTI 프롬프트를 설계하면서 같은 정보도 전달 방식에 따라 사용자 경험이 크게 달라진다는 점이 인상적이었습니다. 짧은 기간이었지만 데이터 수집부터 임베딩, 검색, UI까지 전체 AI 서비스 파이프라인을 경험할 수 있었던 값진 프로젝트였습니다.

> **김서현** — 팀원 각자가 카드사 데이터를 수집하고 전처리하는 과정에서 실제 금융 데이터의 복잡성을 체감했습니다. RAG 파이프라인을 직접 구축하며 단순 LLM 활용을 넘어 hallucination을 줄이는 것이 얼마나 중요한지 깨달았습니다. 16가지 MBTI 프롬프트를 설계하면서 같은 정보도 전달 방식에 따라 사용자 경험이 크게 달라진다는 점이 인상적이었습니다. 짧은 기간이었지만 데이터 수집부터 임베딩, 검색, UI까지 전체 AI 서비스 파이프라인을 경험할 수 있었던 값진 프로젝트였습니다.

> **박지현** — LLM을 활용하여 프롬프트 엔지니어링을 해보며, 이전에 GPT 내부에서 프롬프트 작성을 통해 만들었던 챗봇보다 완성도 높은 챗봇을 만든 경험이 색달랐습니다. AI 서비스 파이프라인 전 과정에 참여할 수 있어 뜻깊었습니다.

> **신문수** — (회고 내용을 입력해주세요)

> **이근혁** — 그동안 쉽게 이용했던 LLM 서비스를 활용해서 서비스를 직접 만들어 볼 수 있는 프로젝트를 진행할 수 있어서 유의미했습니다. 이번 프로젝트도 잘 이끌어주는 팀장님과 믿고 따르는 팀원들과 함께할 수 있어서 즐겁게 진행했습니다.

<br>

---

<div align="center">
  <b>SK Networks AI Camp 25기 · 6팀 · 3차 미니 프로젝트</b><br>
  <i>Our journey continues...</i>
</div>
