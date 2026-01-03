import os
import warnings
import logging
import sys
sys.stdout.reconfigure(encoding="utf-8")
from rag.ingestion import load_pdfs, chunk_documents
from rag.embeddings import embed_and_store
from qdrant_client import QdrantClient
from config.settings import QDRANT_URL, QDRANT_API_KEY
from qdrant_client import QdrantClient
from config.settings import QDRANT_PATH
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
COLLECTION_NAME = "maintenance_docs"
assert client.collection_exists(COLLECTION_NAME), \
    "Collection does not exist. Run create_collection.py first."    
def main():
    docs = load_pdfs()
    chunks = chunk_documents(docs)
    embed_and_store(chunks)
    client.close()
    print("Qdrant client closed")
if __name__ == "__main__":
    main()

