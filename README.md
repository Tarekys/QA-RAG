# QA-RAG: Document Question-Answering Application

QA-RAG is a powerful and user-friendly Streamlit application designed for question-answering over documents. It enables users to upload PDF or TXT files, or query pre-loaded documents stored in the `Data` folder, to retrieve precise answers using advanced retrieval-augmented generation (RAG) techniques. The application leverages **LLaMA-Index** for efficient document indexing and **Google Gemini API** for robust natural language processing.

---

## Features

- **Document Upload**: Upload PDF or TXT files for real-time question-answering.
- **Pre-loaded Documents**: Query documents stored in the `Data` folder without manual uploads.
- **Advanced RAG Pipeline**: Combines document indexing with retrieval and generative AI for accurate answers.
- **Streamlit Interface**: Intuitive web-based UI for seamless user interaction.
- **Scalable Indexing**: Powered by LLaMA-Index for efficient document processing and retrieval.
- **Natural Language Processing**: Utilizes Google Gemini API for high-quality query understanding and response generation.

---

## Prerequisites

Before running the application, ensure you have the following:

- **Python**: Version 3.12 or higher
- **Google Gemini API Key**: Obtain an API key from [Google Cloud](https://cloud.google.com).
- **Dependencies**: Install required Python packages listed in `requirements.txt`.

---

## Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Interface**:
   Open your browser and navigate to `http://localhost:8501`.

3. **Interact with the App**:
   - **Upload a File**: Use the file uploader to add TXT document.
   - **Select Pre-loaded Documents**: Choose from documents in the `Data` folder.
   - **Ask Questions**: Enter your question in the text input field to receive answers based on the document content.


## Dependencies
Key libraries used in the project (listed in `requirements.txt`):
- `streamlit`: Web application framework
- `llama-index`: Document indexing and retrieval
- `google-generativeai`: Google Gemini API for NLP
- `python-dotenv`: Environment variable management

Install all dependencies using:
```bash
pip install -r requirements.txt
```
