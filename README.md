# 🔧 Maintenance Knowledge RAG Assistant for Technicians

A **production-grade Retrieval-Augmented Generation (RAG) system** deployed on the cloud that enables technicians and engineers to query maintenance manuals and technical documents with **accurate, hallucination-free answers**.

This project demonstrates a **fully deployed end-to-end AI application**, covering document ingestion, vector search, cloud-hosted retrieval, LLM-based generation, backend APIs, and a modern web interface.

---

## 🌐 Live Demo

🚀 **Deployed on Render:**  
👉 https://your-render-app-url.onrender.com  
*(Link will be updated)*

To test the RAG
- You can as questions like - (From my uploaded documents on airline manuals)
“How to replace a hydraulic pump?”
“What causes landing gear extension failure?”
“What are engine oil servicing steps?”
---

## 🚀 Key Features

- 📄 PDF ingestion and semantic chunking  
- 🔍 Vector similarity search using **Qdrant Cloud**  
- 🧠 Retrieval-Augmented Generation (RAG) for grounded responses  
- ⚡ Ultra-fast LLM inference using **Groq**  
- 🌐 Flask backend with REST API  
- 🖥️ Professional landing page + interactive chat UI  
- 🔐 Secure configuration using environment variables  
- ☁️ Fully deployed cloud-native architecture  

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** combines:
1. **Information Retrieval** – fetches relevant document chunks from a vector database  
2. **Language Generation** – generates answers strictly grounded in retrieved content  

This ensures:
- ❌ No hallucinations  
- ✅ Traceable, document-backed answers  
- ✅ High reliability for technical and industrial use cases  

---

## 🏗️ System Architecture
User (Browser)
↓
Home Page / Chat UI (HTML, CSS, JS)
↓
Flask Backend (Render Deployment)
↓
Retriever (Sentence Transformers)
↓
Qdrant Cloud (Vector Database)
↓
Groq LLM (Hosted Inference)
↓
Grounded Answer + Sources

---

## 🧰 Tech Stack

### Backend
- Python
- Flask

### Vector Database
- Qdrant Cloud

### Embeddings
- Sentence Transformers (`all-MiniLM-L6-v2`)

### LLM Inference
- Groq (`llama3-8b-8192`)

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### Deployment
- **Render (Flask App Hosting)**
- Qdrant Cloud
- Groq API

---

## 📁 Project Structure

├── app.py # Flask entry point
├── requirements.txt
├── README.md
│
├── config/
│ └── settings.py # Environment-based configuration
│
├── rag/
│ ├── ingestion.py # PDF loading
│ ├── embeddings.py # Vector embedding & storage
│ ├── retriever.py # Similarity search
│ └── generator.py # Groq LLM generation
│
├── templates/
│ ├── index.html # Home / landing page
│ └── chat.html # Chat UI
│
├── static/
│ ├── css/
│ │ ├── home.css
│ │ └── chat.css
│ └── js/
│ ├── home.js
│ └── chat.js
│
├── data/
│ └── *.pdf # Maintenance documents
│
├── create_collection.py # Create Qdrant collection
├── run_ingestion.py # Ingest documents into Qdrant
└── test_rag.py # RAG pipeline test

