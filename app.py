import streamlit as st
import os
from llama_index.core import SimpleDirectoryReader
from data_ingestion import load_data
from embedding_model import download_gemini_embedding
from model_api import load_model

# Page setup css
st.set_page_config(page_title="QA with Docs", layout="centered", page_icon="📄")
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main-header {
        color: #1e3a8a;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-text {
        color: #4b5563;
        font-size: 16px;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
    }
    .stTextInput>div>input {
        border-radius: 10px;
        border: 1px solid #d1d5db;
        padding: 10px;
    }
    .stFileUploader {
        border: 2px dashed #d1d5db;
        border-radius: 10px;
        padding: 20px;
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-header"> QA with Docs</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Upload a document or use files in the "Data" folder to get answers!</div>', unsafe_allow_html=True)

# File uploader
doc = st.file_uploader("Upload a document (optional)", type=["pdf", "txt"])

# Question input
user_question = st.text_input("", placeholder="Ask your question here...")

# Process button
if st.button("Submit"):
    if not user_question:
        st.error("Please enter a question!")
    else:
        with st.spinner("Processing..."):
            try:
                if doc is None:
                    document = load_data("Data")
                else:
                    file_extension = os.path.splitext(doc.name)[1].lower()
                    temp_file_name = f"temp_uploaded_file{file_extension}"
                    with open(temp_file_name, "wb") as f:
                        f.write(doc.read())
                    document = SimpleDirectoryReader(input_files=[temp_file_name]).load_data()

                model = load_model()
                query_engine = download_gemini_embedding(model, document)
                response = query_engine.query(user_question)

                st.markdown("#### Answer:")
                st.write(response.response)

                if os.path.exists(temp_file_name):
                    os.remove(temp_file_name)

            except Exception as e:
                st.error(f"Error: {str(e)}")
                if 'temp_file_name' in locals() and os.path.exists(temp_file_name):
                    os.remove(temp_file_name)
    
    