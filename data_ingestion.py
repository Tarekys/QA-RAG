from llama_index.core import SimpleDirectoryReader
import sys
from logger import logging

def load_data(data):
    """
    Load PDF documents from a specific directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise Exception(f"Error loading data: {str(e)}") from e