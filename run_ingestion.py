import os
import uuid
import pdfplumber
from qdrant_client import QdrantClient
from rag.embeddings import embed_texts
from config.settings import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

DATA_DIR = "data"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

def chunk_text(text, size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def ingest():
    all_chunks = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            print(f"[INFO] Reading {file}")
            text = extract_text(os.path.join(DATA_DIR, file))
            chunks = chunk_text(text)
            all_chunks.extend(chunks)

    print(f"[INFO] Total chunks: {len(all_chunks)}")

    vectors = embed_texts(all_chunks)

    points = []
    for text, vector in zip(all_chunks, vectors):
        points.append({
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {"text": text}
        })

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"[SUCCESS] Inserted {len(points)} points")

if __name__ == "__main__":
    ingest()