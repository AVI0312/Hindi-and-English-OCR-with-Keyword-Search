# -*- coding: utf-8 -*-
"""iitr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wWGsU00rwo-WhsLrkqp9a6_KGy1D-uQX
"""

!apt-get update
!apt-get install -y tesseract-ocr
!pip install pytesseract pillow gradio

import gradio as gr
import pytesseract
from PIL import Image
import re
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    return extracted_text

def search_keywords(extracted_text, keyword):
    # Escape the keyword for regex and create a pattern with word boundaries
    keyword_pattern = r'\b' + re.escape(keyword) + r'\b'

    # Highlight the keyword in the entire extracted text
    highlighted_text = re.sub(
        keyword_pattern,
        lambda match: f'**<span style="background-color: red;">{match.group(0)}</span>**',
        extracted_text,
        flags=re.IGNORECASE
    )

    # Check if the keyword is found and return formatted output
    if keyword.lower() in extracted_text.lower():
        return f"n\nFound '{keyword}' in the text:\n{highlighted_text}"
    else:
        return f"'{keyword}' not found in the text."


def ocr_search(image, keyword):
    extracted_text = extract_text(image)
    search_result = search_keywords(extracted_text, keyword)
    return extracted_text, search_result

interface = gr.Interface(
    fn=ocr_search,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(lines=1, placeholder="Enter keyword to search", label="Keyword")
    ],
    outputs=[
        gr.Markdown(label="Extracted Text"),
        gr.Markdown(label="Search Result")
    ],
    title="Hindi and English OCR with Keyword Search",
    description="Upload an image containing text in Hindi and English. Enter a keyword to search within the extracted text."
)

# Launch the interface
interface.launch(share=True)