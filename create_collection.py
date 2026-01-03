from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from config.settings import COLLECTION_NAME, QDRANT_PATH
from qdrant_client import QdrantClient
from config.settings import QDRANT_URL, QDRANT_API_KEY
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)
client.close() 
print("Collection created:", COLLECTION_NAME)
