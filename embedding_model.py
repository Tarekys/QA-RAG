from llama_index.core import VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import StorageContext, load_index_from_storage

from data_ingestion import load_data
from model_api import load_model
from logger import logging

def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Parameters:
    - model: The language model (e.g., Gemini model) to use.
    - document: The list of documents to index.

    Returns:
    - QueryEngine: A query engine for efficient similarity queries.
    """
    try:
        logging.info("Initializing Gemini embedding model...")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        
        logging.info("Creating vector index from documents...")
        index = VectorStoreIndex.from_documents(
            document,
            llm=model,
            embed_model=gemini_embed_model,
            chunk_size=512,
            chunk_overlap=20
        )

        logging.info("Persisting index to storage...")
        index.storage_context.persist(persist_dir="storage")
        
        logging.info("Creating query engine...")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        logging.error(f"Error in creating index or query engine: {str(e)}")
        raise Exception(f"Failed to create query engine: {str(e)}") from e