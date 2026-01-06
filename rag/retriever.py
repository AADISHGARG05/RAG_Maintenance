from qdrant_client import QdrantClient
from config.settings import (
    QDRANT_URL,
    QDRANT_API_KEY,
    COLLECTION_NAME,
    TOP_K
)
from rag.embeddings import embed_query

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

def retrieve_relevant_chunks(query):
    # Embed query using SAME model as ingestion
    query_vector = embed_query(query)

    # CORRECT API — query_points (NOT search)
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=TOP_K,
        with_payload=True
    )

    contexts = []
    sources = []

    for point in response.points:
        payload = point.payload or {}
        if "text" in payload:
            contexts.append(payload["text"])
            sources.append(point.id)

    return contexts, sources