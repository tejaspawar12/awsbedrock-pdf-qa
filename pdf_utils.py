# pdf_utils.py

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf_text(file_path: str) -> str:
    """
    Extract all text from a PDF file using PyPDF2.
    Returns the full combined text from all pages.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        print(f"❌ Error loading PDF: {e}")
        return ""

def split_text_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50):
    """
    Split the input text into overlapping chunks.
    These are useful for embedding, graph construction, and retrieval.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return splitter.split_text(text)
