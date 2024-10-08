from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env.

import streamlit as st
import os
from PIL import Image  # Import for image processing

import google.generativeai as genai  # Google's Generative AI library

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the new Gemini model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Use the updated model
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

# Get user input and image
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Load and display the image
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# Generate response when button is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
