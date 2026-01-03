from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from config.settings import COLLECTION_NAME, QDRANT_PATH
from qdrant_client import QdrantClient
from config.settings import QDRANT_URL, QDRANT_API_KEY
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
def embed_and_store(chunks):
    points = []

    for idx, chunk in enumerate(chunks):
        vector = model.encode(chunk["text"]).tolist()

        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "text": chunk["text"],
                    "source": chunk["metadata"]["source"],
                    "page": chunk["metadata"]["page"]
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
