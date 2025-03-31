# app.py
import streamlit as st
from rag_pipeline import run_rag_pipeline
from pdf_utils import load_pdf_text, split_text_into_chunks
from neo4j_utils import Neo4jConnection
from vector_store import store_embeddings
import hashlib

st.set_page_config(page_title="PDF Q&A Chatbot", page_icon="📄")
st.title("📚 Chat with your PDF (Powered by RAG + Neo4j + Bedrock)")

# Utility to compute hash of uploaded PDF (avoid reprocessing same file)
def compute_file_hash(file_bytes: bytes) -> str:
    return hashlib.md5(file_bytes).hexdigest()

# Reset functionality
if st.button("Reset App"):
    st.session_state.clear()
    st.experimental_rerun()

# Step 1: Upload PDF
pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file:
    # Convert file to bytes for hashing
    pdf_bytes = pdf_file.read()
    current_file_hash = compute_file_hash(pdf_bytes)

    # Check if we've processed a PDF before
    if "processed_file_hash" not in st.session_state or st.session_state.processed_file_hash != current_file_hash:
        # The user uploaded a new PDF or the first PDF in this session
        with open("temp.pdf", "wb") as f:
            f.write(pdf_bytes)

        text = load_pdf_text("temp.pdf")
        chunks = split_text_into_chunks(text)
        st.success(f"📄 PDF uploaded and split into {len(chunks)} chunks.")

        # Build graph/store
        with st.spinner("📌 Creating knowledge graph and vector store..."):
            conn = Neo4jConnection()
            conn.clear_all_chunks()  # Clear old data
            conn.store_chunks(chunks)
            conn.close()
            store_embeddings(chunks)

        st.session_state.processed_file_hash = current_file_hash
        st.success("✅ Knowledge graph and vector store created!")
    else:
        st.info("✅ This PDF has already been processed in this session.")

    # Step 3: Chat UI
    st.header("💬 Chat with your PDF")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for user_msg, bot_msg in st.session_state.chat_history:
        st.chat_message("user").write(user_msg)
        st.chat_message("assistant").write(bot_msg)

    user_question = st.chat_input("Ask a question about your PDF")

    if user_question:
        with st.chat_message("user"):
            st.write(user_question)

        with st.spinner("🤖 Thinking..."):
            answer = run_rag_pipeline(user_question)

        with st.chat_message("assistant"):
            st.write(answer)

        # Save to session state
        st.session_state.chat_history.append((user_question, answer))
