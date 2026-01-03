from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from config.settings import COLLECTION_NAME, QDRANT_HOST, QDRANT_PORT

def get_qdrant_client():
    return QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT
    )

def create_collection_if_not_exists(vector_size: int):
    client = get_qdrant_client()
    
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )
