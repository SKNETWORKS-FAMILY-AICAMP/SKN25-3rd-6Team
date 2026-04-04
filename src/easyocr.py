import os
import easyocr
import numpy as np
from pdf2image import convert_from_path
from langchain_core.documents import Document


# OCR 리더는 한 번만 생성
reader = easyocr.Reader(['ko', 'en'], gpu=False, verbose=False)


def ocr_pdf_easyocr(file_path: str):
    """
    PDF 1개를 OCR해서 텍스트 반환
    """
    images = convert_from_path(file_path)
    full_text = ""

    for i, image in enumerate(images):
        try:
            image_np = np.array(image)
            result = reader.readtext(image_np, detail=0)

            if not result:
                print(f"[WARN] 페이지 {i+1} OCR 결과 없음: {file_path}")
                continue

            text = " ".join(result).strip()

            if text:
                full_text += text + "\n"

        except Exception as e:
            print(f"[ERROR] {file_path} - page {i+1}: {e}")

    return full_text.strip()


def save_ocr_pdfs_to_txt(pdf_folder: str, output_folder: str):
    """
    OCR 대상 PDF 폴더를 OCR하여 txt 파일로 저장
    """
    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(pdf_folder):
        raise FileNotFoundError(f"폴더가 존재하지 않습니다: {pdf_folder}")

    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            print(f"[OCR] {filename}")

            text = ocr_pdf_easyocr(file_path)

            if not text.strip():
                print(f"[SKIP] 텍스트 없음: {filename}")
                continue

            save_name = filename.replace(".pdf", ".txt")
            save_path = os.path.join(output_folder, save_name)

            with open(save_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"[SAVE] {save_name}")


def save_ocr_docs_to_txt(ocr_docs, output_folder: str):
    """
    이미 메모리에 있는 ocr_docs를 txt 파일로 저장
    """
    os.makedirs(output_folder, exist_ok=True)

    for doc in ocr_docs:
        filename = doc.metadata.get("source", "unknown.pdf")
        save_name = filename.replace(".pdf", ".txt")
        save_path = os.path.join(output_folder, save_name)

        text = doc.page_content

        if not text.strip():
            print(f"[SKIP] 빈 문서: {filename}")
            continue

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"[SAVE] {save_name}")


def load_ocr_txt_as_documents(folder_path: str, card_company: str = None):
    """
    OCR 결과 txt 파일을 Document로 로드
    """
    docs = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"폴더가 존재하지 않습니다: {folder_path}")

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".txt"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read().strip()

            if not text:
                print(f"[SKIP] 빈 txt: {filename}")
                continue

            doc = Document(
                page_content=text,
                metadata={
                    "source": filename,
                    "file_path": filepath,
                    "card_name": os.path.splitext(filename)[0],
                    "type": "ocr",
                    "card_company": card_company if card_company else "unknown"
                }
            )
            docs.append(doc)

    print(f"[INFO] OCR txt 문서 수: {len(docs)}")
    return docs