#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import gradio as gr
from PIL import Image
import pytesseract
import re
import json

# Initialize the OCR model (Using Tesseract in this example for Hindi + English)
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image, lang='hin+eng')
    return text


# In[9]:


def search_text(extracted_text, keyword):
    if not keyword.strip():
        return "Please enter a keyword to search."

    if keyword.lower() not in extracted_text.lower():
        return f"The searched text '{keyword}' was not found."

    # If the keyword is found, highlight it in red
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    highlighted_text = pattern.sub(f'<span style="background-color: red; color: white;">{keyword}</span>', extracted_text)
    return highlighted_text


# In[10]:


def process_image(image, keyword):
    # Extract text
    extracted_text = extract_text_from_image(image)
    
    # Search for keyword
    search_result = search_text(extracted_text, keyword)
    
    # Prepare the JSON output
    json_output = json.dumps({"EXTRACTED_TEXT": extracted_text}, ensure_ascii=False, indent=4)
    
    return json_output, search_result

# Gradio Interface
interface = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="pil"), gr.Textbox(label="Enter Keyword")],
    outputs=[gr.JSON(label="Extracted Text (JSON)"), gr.HTML(label="Highlighted Search Result")],
    title="OCR and Keyword Search Application",
    description="Upload an image with text in Hindi and English. Extract text and search keywords in the extracted text."
)

# Launch Gradio App
interface.launch(share=True)


# In[ ]:




