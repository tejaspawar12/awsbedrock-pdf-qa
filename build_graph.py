from pdf_utils import load_pdf_text, split_text_into_chunks
from neo4j_utils import Neo4jConnection
from vector_store import store_embeddings

pdf_path = "A:/AWSBedrock/Project2/sample.pdf"
text = load_pdf_text(pdf_path)
chunks = split_text_into_chunks(text)

# Neo4j
neo4j_conn = Neo4jConnection()
neo4j_conn.clear_all_chunks()  # optional
neo4j_conn.store_chunks(chunks)
neo4j_conn.close()

# FAISS
store_embeddings(chunks)

print(f"✅ Added {len(chunks)} chunks to Neo4j and stored in FAISS.")
