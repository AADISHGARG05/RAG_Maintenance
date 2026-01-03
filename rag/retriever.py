from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from config.settings import QDRANT_URL, QDRANT_API_KEY
from qdrant_client import QdrantClient
from config.settings import (
    COLLECTION_NAME,
    QDRANT_PATH,
    TOP_K,
    SCORE_THRESHOLD
)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
def retrieve_relevant_chunks(query: str):
    query_vector = model.encode(query).tolist()
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=TOP_K
    ).points
    contexts = []
    sources = []

    for r in results:
        contexts.append(r.payload["text"])
        sources.append(
        f"{r.payload['source']} (page {r.payload['page']})"
    )
    sources = list(dict.fromkeys(sources))
    client.close()
    return contexts, list(sources)