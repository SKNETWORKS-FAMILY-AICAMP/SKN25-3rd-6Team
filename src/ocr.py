import os
from openai import OpenAI
from pdf2image import convert_from_path
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import dotenv
import base64

dotenv.load_dotenv()

client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(BASE_DIR, "../data/raw/ibk/IBK_I-Anywhere_Green_Card_Guide.pdf")
pages = convert_from_path(pdf_path)

# pdf page OCR
for i, page in enumerate(pages):
    buffer = BytesIO() # 메모리에 가상 파일 생성
    page.save(buffer, format="PNG") # 메모리에 저장
    img_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Vision API
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{img_data}"
                    },
                    {
                        "type": "input_text",
                        "text": "이 이미지에서 텍스트를 전부 추출해줘."
                    }
                ]
            }
        ]

    )
    print(f"{i+1}page : {response.output_text}")

# TODO : 저장 경로 방식 결정 필요
# TODO : 모델 설정