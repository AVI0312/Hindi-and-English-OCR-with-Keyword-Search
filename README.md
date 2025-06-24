# Hindi-and-English-OCR-with-Keyword-Search

A OCR application that extracts text from images and allows keyword searching within the extracted text. Built with Gradio for a seamless user experience.

##  Project Overview

This project provides an OCR-based solution for extracting text from images, with the added functionality of searching for specific keywords within the extracted text. It supports both Hindi and English languages, making it versatile for diverse use cases. The application is built using Gradio, offering an intuitive interface for users to interact with the tool easily.

###  Key Features

- **Text Extraction:** Extracts text from images using Tesseract OCR.
- **Multilingual Support:** Supports both Hindi and English languages.
- **Keyword Search:** Search for specific keywords within the extracted text.
- **Highlighting:** Keywords found in the text are highlighted for easy identification.
- **JSON Output:** Provides extracted text in JSON format for further processing.
- **User-Friendly Interface:** Gradio-based interface for easy interaction.

###  Tech Stack

- **Frontend:** Gradio
- **OCR Engine:** Tesseract OCR
- **Image Processing:** Pillow (PIL)
- **Text Processing:** Regular Expressions
- **Data Handling:** JSON

###  Installation

1. **Prerequisites:**
   - Python 3.8+
   - Tesseract OCR installed on your system
   - Required Python packages

2. **Install Dependencies:**
   ```bash
   pip install gradio pytesseract Pillow
   ```

3. **Clone the Repository:**
   ```bash
   git clone [your-repository-url]
   cd iitrproject
   ```

###  Usage

1. **Run the Application:**
   ```bash
   python iitrproject.py
   ```
2. **Access the Interface:**
   - Open a web browser and navigate to the URL provided by Gradio (typically `http://localhost:7860`).

3. **Using the Interface:**
   - **Upload an Image:** Click on the image upload button to select an image file.
   - **Enter Keyword:** Type the keyword you want to search for in the text input field.
   - **Process Image:** Click the "Process Image" button to extract text and search for the keyword.
   - **View Results:** Results are displayed in both JSON and HTML formats.


  
![Screenshot 2024-09-28 145703](https://github.com/user-attachments/assets/dab3da36-1ef4-40c2-a9fa-bef5fbe6ef69)
![Screenshot 2024-09-28 143325](https://github.com/user-attachments/assets/bb381d40-4a22-4a9e-8624-5df738c6fef1)
![Screenshot 2024-09-28 143351](https://github.com/user-attachments/assets/d6351355-6493-4580-a436-eb31043c7af8)



