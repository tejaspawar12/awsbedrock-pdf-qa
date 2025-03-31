# rag_pipeline.py

from bedrock_llm import get_bedrock_llm
from neo4j_utils import Neo4jConnection
from langchain_core.messages import HumanMessage
from vector_store import retrieve_relevant_chunks
import textwrap

def run_rag_pipeline(user_question: str):
    """
    RAG Pipeline using Claude 2.1 via Bedrock + FAISS vector search.
    """

    # Step 1: Load chunks from Neo4j (optional if FAISS is primary)
    conn = Neo4jConnection()
    chunks = conn.get_all_chunks()
    conn.close()

    if not chunks:
        return "❌ No chunks found in the knowledge graph."

    # Step 2: Retrieve semantically similar chunks
    relevant_chunks = retrieve_relevant_chunks(user_question, k=5)

    if not relevant_chunks:
        return "🤖 Sorry, no relevant content found in the PDF."

    # Step 3: Create Claude-optimized prompt
    context = "\n\n".join(relevant_chunks)
    
    prompt = textwrap.dedent(f"""
    Human: You are a helpful AI assistant. Use only the information in the context below to answer the question.

    If the answer is not found in the context, respond with:
    "I'm sorry, the document does not provide enough information to answer that question."

    ---------------------
    Context:
    {context}
    ---------------------

    Question: {user_question}
    Answer:
    """).strip()

    # Step 4: Get response from Claude
    llm = get_bedrock_llm()
    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content.strip()
