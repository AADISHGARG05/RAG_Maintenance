import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCUMENTS_PATH = os.path.join(BASE_DIR, "data", "documents")
COLLECTION_NAME = "maintenance_docs"
OLLAMA_MODEL = "llama3"
MIN_SCORE = 0.25  
COLLECTION_NAME = "maintenance_docs"
QDRANT_PATH = "./vector_store"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 8
SCORE_THRESHOLD = 0.35
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
