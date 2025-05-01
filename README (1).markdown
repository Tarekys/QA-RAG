# QA-RAG: Document Question-Answering Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red) ![LLaMA-Index](https://img.shields.io/badge/LLaMA--Index-0.8%2B-green) ![Google Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-Latest-yellow) ![License](https://img.shields.io/badge/License-MIT-blue)

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

- **Python**: Version 3.8 or higher
- **Google Gemini API Key**: Obtain an API key from [Google Cloud](https://cloud.google.com).
- **Dependencies**: Install required Python packages listed in `requirements.txt`.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/qa-rag.git
   cd qa-rag
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your Google Gemini API key:
   ```
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

5. **Prepare Documents** (optional):
   Place PDF or TXT files in the `Data` folder for pre-loaded document querying.

---

## Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Interface**:
   Open your browser and navigate to `http://localhost:8501`.

3. **Interact with the App**:
   - **Upload a File**: Use the file uploader to add a PDF or TXT document.
   - **Select Pre-loaded Documents**: Choose from documents in the `Data` folder.
   - **Ask Questions**: Enter your question in the text input field to receive answers based on the document content.

---

## Project Structure

```
qa-rag/
├── Data/                    # Folder for pre-loaded PDF/TXT documents
├── app.py                   # Main Streamlit application script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not tracked)
├── README.md                # Project documentation
└── ...                      # Other supporting files
```

---

## Dependencies

Key libraries used in the project (listed in `requirements.txt`):
- `streamlit`: Web application framework
- `llama-index`: Document indexing and retrieval
- `google-generativeai`: Google Gemini API for NLP
- `PyPDF2`: PDF file processing
- `python-dotenv`: Environment variable management

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Configuration

- **Google Gemini API**: Ensure the API key is correctly set in the `.env` file.
- **Data Folder**: The `Data` folder is automatically scanned for PDF and TXT files. Add or remove files as needed.
- **Indexing Settings**: Modify indexing parameters in `app.py` (e.g., chunk size, embedding model) for performance tuning.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **LLaMA-Index**: For providing a robust framework for document indexing and retrieval.
- **Google Gemini API**: For powering natural language understanding and generation.
- **Streamlit**: For enabling rapid development of interactive web applications.

---

## Contact

For questions or support, please open an issue on the [GitHub repository](https://github.com/yourusername/qa-rag) or contact [your.email@example.com](mailto:your.email@example.com).