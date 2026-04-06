# SKN25-3rd-6Team
## 01. 프로젝트 소개

## 💳 PickCardU
> **"복잡한 신용카드 혜택, 당신의 소비 습관(MBTI)으로 똑똑하게 큐레이션 하세요."**

**PickCardU**는 신용카드 시장의 정보 불균형을 해소하기 위해, **RAG(Retrieval-Augmented Generation)** 기술을 활용하여 사용자에게 최적의 카드를 추천하고 관리해 주는 AI 기반 개인 맞춤형 신용카드 큐레이션 시스템입니다.

---

## 🛠 Tech Stack
| 구분 | 기술 스택 |
| :--- | :--- |
| **Frontend** | Streamlit, Figma |
| **Backend** | Python, LangChain, OpenAI (GPT-4o) |
| **Database/Infra** | ChromaDB (Vector DB), SQLite, Docker |
| **Data/Tools** | PyPDFLoader, Unstructured, Git, Notion, VSCode |

---

## 🏗 System Architecture
서비스는 크게 데이터를 정제하고 벡터화하는 **데이터 파이프라인**과, 사용자 요청을 처리하는 **RAG/LLM 파이프라인**으로 구성됩니다.

### 1. 데이터 파이프라인
* 10개 주요 카드사의 상품 설명서 PDF 수집 및 전처리.
* `Unstructured`와 `PyPDFLoader`를 사용하여 표(Table)와 텍스트를 구조적으로 추출.
* `text-embedding-3-small` 모델을 사용하여 벡터화 후 `ChromaDB`에 저장.

### 2. RAG & LLM 파이프라인
* **검색 전략:** 유사도 기반 검색 및 카드명 그룹화, 키워드 필터링을 통해 검색 정확도 최적화.
* **MBTI 페르소나:** 16가지 MBTI 성향별 맞춤 프롬프트를 적용하여 공감형/분석형 등 개인화된 답변 제공.
* **할루시네이션 방지:** 추출된 데이터(Context) 내 정보만 참조하도록 제약하여 정확한 정보 전달.

---

## ✨ Key Features
* **개인 맞춤형 카드 큐레이션:** 사용자의 소비 패턴과 MBTI를 분석하여 최적의 카드 추천.
* **보유 카드 질의응답:** 등록된 카드의 혜택 조건을 즉시 확인 가능한 스마트 Q&A.
* **데이터 신뢰성:** 카드사 공식 PDF 공시 자료를 기반으로 한 정확한 정보 제공.
* **사용자 친화적 페르소나:** T형(논리/효율), F형(공감/조언) 등 성향별 맞춤 응답 스타일 적용.

---

## 👥 Team Members
| 역할 | 팀원 | 주요 역할 |
| :--- | :--- | :--- |
| **PM / UI** | 박연정 | 서비스 아키텍처 설계, UI/UX 디자인, Docker 환경 세팅 |
| **Backend** | 김서현 | 데이터 수집(삼성, 하나), 임베딩 및 벡터DB 구축 |
| **Prompt** | 박지현 | 프롬프트 엔지니어링, 발표 총괄 및 PPT 제작 |
| **Data** | 신문수 | 데이터 수집(NH, BC), OCR/PDF 텍스트 정제 및 청킹 |
| **DB** | 이근혁 | SQLite DB 설계, 프롬프트 테스트 및 시스템 개선 |

---

## 📅 Project Roadmap
* **Step 1:** 카드사별 상품 설명서 수집 및 PDF 전처리 파이프라인 구축.
* **Step 2:** RAG 체인 구현 및 벡터 DB 임베딩 최적화.
* **Step 3:** MBTI 기반 페르소나 설정 및 프롬프트 엔지니어링.
* **Step 4:** Streamlit 기반 서비스 UI 개발 및 SQLite 연동.
* **Step 5:** 시연 테스트 및 성능 개선(최종 발표).

---

## 🚀 How to Run
