# vector_store.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import BedrockEmbeddings
from langchain.docstore.document import Document
import os

# Location to save FAISS index
FAISS_PATH = "faiss_index"

def store_embeddings(chunks):
    """
    Converts text chunks to embeddings and stores in FAISS.
    """
    texts = [Document(page_content=chunk) for chunk in chunks]

    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",  # ✅ Specify embedding model
        region_name="us-east-1"  # 🔁 Make sure this matches your region
    )

    faiss_index = FAISS.from_documents(texts, embeddings)
    faiss_index.save_local(FAISS_PATH)
    print("✅ Stored chunks in FAISS vector store.")

def retrieve_relevant_chunks(query, k=5):
    """
    Retrieves semantically similar chunks to the query from FAISS.
    """
    if not os.path.exists(FAISS_PATH):
        raise ValueError("FAISS index not found. Please store embeddings first.")

    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name="us-east-1"
    )

    faiss_index = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = faiss_index.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]
