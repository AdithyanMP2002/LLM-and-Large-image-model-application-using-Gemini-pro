To successfully execute your project in the correct order using the files you’ve provided, follow these steps:

### Step 1: **Prepare Your Environment**
Before running any files, ensure that you have the required libraries installed and that your environment is correctly configured.

```bash
pip install streamlit google-generativeai python-dotenv pillow
```

Make sure your `.env` file is in place with your `GOOGLE_API_KEY`:

```plaintext
GOOGLE_API_KEY=your_google_api_key_here
```

### Step 2: **Execute Files in Order**

#### 1. **Run `app.py`**
   - **Purpose**: This sets up a basic Q&A chatbot using text input.
   - **Command**:
     ```bash
     streamlit run app.py
     ```
   - **Check**: Ensure the app launches and responds to text input.

#### 2. **Run `chat.py`**
   - **Purpose**: Extends the chatbot to maintain a conversation history within a single session.
   - **Command**:
     ```bash
     streamlit run chat.py
     ```
   - **Check**: Ensure the conversation history is maintained within a session.

#### 3. **Run `qachat.py`**
   - **Purpose**: Maintains the chat history across interactions using Streamlit's session state.
   - **Command**:
     ```bash
     streamlit run qachat.py
     ```
   - **Check**: Verify that the chat history persists even after multiple interactions.

#### 4. **Run `vision.py`**
   - **Purpose**: Adds image input functionality, allowing the model to generate responses based on both text and image inputs.
   - **Command**:
     ```bash
     streamlit run vision.py
     ```
   - **Check**: Test with an image upload and an optional text input to ensure the model generates appropriate content.

### Step 3: **Testing and Final Checks**
- Interact with each Streamlit app in your browser to verify that all functionalities work as expected.
- Ensure that the conversation history, text, and image processing all function smoothly.
- If everything works correctly, your project is successfully executed!

Let me know if you encounter any issues or need further assistance!
