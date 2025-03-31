# 📃 Chat with Your PDF (Powered by RAG + Neo4j + AWS Bedrock Claude 2.1)

An interactive Streamlit application that lets you chat with any PDF using a Retrieval-Augmented Generation (RAG) pipeline backed by FAISS, Neo4j, and AWS Bedrock (Claude 2.1).

---

## 🚀 Features

- 📄 Upload and process any PDF
- 🧠 Semantic chunking and vector storage using FAISS
- 📈 Knowledge graph generation with Neo4j
- 🔍 Contextual search based on Titan embeddings
- 💬 Claude 2.1 LLM (via AWS Bedrock) for accurate Q&A
- 🧵 Chat history preserved during session

---

## 💪 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: Claude 2.1 (`anthropic.claude-v2:1`) via AWS Bedrock
- **Embeddings**: Amazon Titan Text Embedding v1
- **Vector Store**: FAISS
- **Graph Store**: Neo4j
- **Middleware**: LangChain

---

## 📂 Project Structure

```
pdf-chatbot-bedrock/
├── app.py                   # Streamlit App UI
├── rag_pipeline.py         # Retrieval + Generation logic
├── bedrock_llm.py          # Claude 2.1 LLM connector
├── vector_store.py         # FAISS storage and search
├── pdf_utils.py            # PDF text extraction and chunking
├── neo4j_utils.py          # Graph generation with Neo4j
├── .env.example            # Template for environment variables
├── requirements.txt        # All dependencies
└── README.md               # Project documentation
```

---

## 🚪 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pdf-chatbot-bedrock.git
cd pdf-chatbot-bedrock
```

### 2. Setup Environment Variables
Create a `.env` file and add your credentials:

```
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

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📸 Screenshots

| Upload & Vectorization | Chat in Action |
|------------------------|----------------|
| ![](assets/screenshots/upload.png) | ![](assets/screenshots/chat.png) |


---

## 🚀 Future Ideas

- [ ] Add support for multiple PDF uploads and document switching
- [ ] Claude 3.5 or Sonnet model upgrade option
- [ ] Highlight chunks used for answers
- [ ] Save chat history across sessions

---

## 👍 Credits

Built using:
- [Streamlit](https://streamlit.io)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [LangChain](https://www.langchain.com/)
- [Neo4j](https://neo4j.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

## 🚪 License

This project is licensed under the [MIT License](LICENSE).

