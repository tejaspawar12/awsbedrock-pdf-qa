# 📚 Chat with Your PDF (Powered by RAG + Neo4j + AWS Bedrock Claude 2.1)

An intelligent PDF Question-Answering system built using Retrieval-Augmented Generation (RAG). It allows users to upload a PDF and interact with it via natural language queries. The system utilizes **Amazon Bedrock Claude 2.1**, **Amazon Titan embeddings**, **FAISS** for vector similarity search, and **Neo4j** to build a lightweight knowledge graph.

---

## 🚀 Features

- 📄 Upload any PDF document
- 🧠 Extract and split content into semantic chunks
- 🧲 Embed text chunks with Titan embedding via AWS Bedrock
- 🧮 Store embeddings in FAISS for vector-based retrieval
- 🌐 Build a knowledge graph using Neo4j from PDF context
- 💬 Use Claude 2.1 (via Bedrock) for accurate Q&A
- 🗂️ Session-persistent chat interface via Streamlit
- ♻️ Avoids redundant reprocessing using file hashing

---

## 🧰 Tech Stack

| Layer       | Technology                |
|-------------|----------------------------|
| Frontend    | Streamlit                 |
| Backend     | Python                    |
| LLM         | Claude 2.1 via Bedrock    |
| Embeddings  | Amazon Titan Embed Text   |
| Vector DB   | FAISS                     |
| Graph DB    | Neo4j                     |
| Middleware  | LangChain                 |

---

## 📁 Project Structure

```
pdf-chatbot-bedrock/
├── app.py                   # Streamlit App UI
├── rag_pipeline.py         # Retrieval + Claude LLM pipeline
├── bedrock_llm.py          # AWS Bedrock Claude integration
├── vector_store.py         # FAISS storage and embedding logic
├── pdf_utils.py            # PDF parsing and chunking
├── neo4j_utils.py          # Chunk node creation in Neo4j
├── .env.example            # Template for credentials
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🧪 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pdf-chatbot-bedrock.git
cd pdf-chatbot-bedrock
```

### 2. Setup Environment Variables
Create a `.env` file based on `.env.example`:

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1

NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Connect to Neo4j (AuraDB or Local)

#### Option A: Use Neo4j AuraDB (Recommended for Cloud)
1. Go to [https://neo4j.com/cloud/aura/](https://neo4j.com/cloud/aura/)
2. Create a free instance (AuraDB Free Tier)
3. Get your connection credentials:
   - Bolt URI (e.g., `neo4j+s://xxxx.databases.neo4j.io`)
   - Username: `neo4j`
   - Password: (auto-generated)
4. Paste these into your `.env` file:
```env
NEO4J_URI=neo4j+s://xxxx.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

#### Option B: Run Neo4j Locally with Docker
```bash
docker run \
  --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/test \
  neo4j:latest
```bash
docker run \
  --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/test \
  neo4j:latest
```

### 5. Run the App
```bash
streamlit run app.py
```

---

## 🖼️ Screenshots

| PDF Upload & Processing       | Claude Answering a Query         |
|------------------------------|----------------------------------|
| ![](assets/screenshots/upload.png) | ![](assets/screenshots/chat.png) |

---

## ✅ Features in Action

- **File Upload**: Drag-and-drop PDF interface.
- **Chunking & Storage**: Chunking uses RecursiveCharacterTextSplitter, and FAISS indexes embeddings.
- **Neo4j Integration**: Every chunk becomes a node in Neo4j, enabling knowledge graph visualizations.
- **LLM Query**: Claude 2.1 uses context retrieved from FAISS + Neo4j and answers with precision.

---

## 🧠 Prompt Design (Claude 2.1)

```text
Human: You are a helpful AI assistant. Use only the information in the context below to answer the question.

If the answer is not found in the context, respond with:
"I'm sorry, the document does not provide enough information to answer that question."

---------------------
Context:
{{relevant_chunks}}
---------------------

Question: {{user_question}}
Answer:
```

---

## 🔮 Roadmap

- [ ] Switchable LLM support (Claude 3, Titan Text)
- [ ] Multi-PDF support with dropdown selection
- [ ] Neo4j relationship visualization in-app
- [ ] Upload OCR-based scanned PDFs
- [ ] Export full chat history as Markdown or PDF

---

## 📜 License

MIT License. Free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [Neo4j](https://neo4j.com/)
- [Streamlit](https://streamlit.io/)
- [FAISS by Facebook AI](https://github.com/facebookresearch/faiss)

