import subprocess
import pytesseract
from PIL import Image
import cv2
import numpy as np
import requests
from langchain.llms import Ollama

# Path to your Tesseract-OCR executable (ensure it's installed on your Mac)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy (convert to grayscale and apply binary threshold).
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return Image.fromarray(binary_image)
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

def extract_text_from_image(image_path):
    """
    Extracts text content from an image using OCR.
    """
    try:
        preprocessed_image = preprocess_image(image_path)
        if preprocessed_image:
            text = pytesseract.image_to_string(preprocessed_image, lang="eng")
            return text.strip()
        else:
            return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def generate_code_with_ollama(prompt):
    """
    Sends the prompt to the Code Llama model via Ollama and retrieves the output.
    """
    try:
        # Run Ollama CLI to interact with the Code Llama model
        result = subprocess.run(
            ["ollama", "chat", "--model", "codellama", "--input", prompt],
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running Ollama: {e}")
        return None

if __name__ == "__main__":
    # Path to the webpage image
    image_path = "image.png"  # Replace with your image file path

    print("Extracting text from the image...")
    webpage_description = extract_text_from_image(image_path)

    if webpage_description:
        print("\nExtracted Webpage Description:")
        print(webpage_description)

        # Refined prompt for Code Llama
        prompt = f"""
        You are an expert frontend developer. Based on the following description of a webpage, 
        generate the React.js and CSS code to replicate its design.

        Webpage Description:
        {webpage_description}

        Please ensure the React.js code includes proper components, uses Material-UI or plain CSS, 
        and the CSS file styles match the described elements.
        """

        # print("\nSending prompt to Code Llama...")
        # url = "http://localhost:11434/api/generate"
        # payload = {
        #     "model": "codellama",
        #     "prompt": prompt
        #  }
        # generated_code = requests.post(url, json=payload)
        
        llm = Ollama(model="codellama")
        generated_code = llm(prompt)
        # print(response)  

        if generated_code:
            print("\nGenerated React.js and CSS Code:")
            print(generated_code)

            # Save the output to files
            with open("webpage_code.jsx", "w") as react_file:
                react_file.write(generated_code)
            print("\nCode saved to webpage_code.jsx")
        else:
            print("\nFailed to generate code. Please check your Ollama setup or refine the prompt.")
    else:
        print("\nFailed to extract text from the image. Please check the image quality or OCR setup.")
