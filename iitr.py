import streamlit as st
import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    return extracted_text

def search_keywords(extracted_text, keyword):
    keyword_pattern = r'\b' + re.escape(keyword) + r'\b'
    highlighted_text = re.sub(
        keyword_pattern,
        lambda match: f'<span style="background-color: red;">{match.group(0)}</span>',
        extracted_text,
        flags=re.IGNORECASE
    )
    if keyword.lower() in extracted_text.lower():
        return f"Found '{keyword}' in the text:\n{highlighted_text}"
    else:
        return f"'{keyword}' not found in the text."

def ocr_search(image, keyword):
    extracted_text = extract_text(image)
    search_result = search_keywords(extracted_text, keyword)
    return extracted_text, search_result

# Streamlit Interface
st.title("Hindi and English OCR with Keyword Search")
st.write("Upload an image containing text in Hindi and English. Enter a keyword to search within the extracted text.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
keyword = st.text_input("Enter keyword to search")

if uploaded_file is not None and keyword:
    image = Image.open(uploaded_file)
    extracted_text, search_result = ocr_search(image, keyword)
    
    st.subheader("Extracted Text")
    st.write(extracted_text)
    
    st.subheader("Search Result")
    st.markdown(search_result, unsafe_allow_html=True)
