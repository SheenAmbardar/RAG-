
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parents[3]
DB_PATH = ROOT / "data" / "chroma_db"

client = chromadb.PersistentClient(path=str(DB_PATH))
collection = client.get_or_create_collection("sentinel_documents")

@__import__("functools").lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def add_documents(documents):
    documents = [d.strip() for d in documents if d.strip()]
    if not documents:
        return 0

    model = get_model()
    embeddings = model.encode(documents).tolist()

    import uuid
    ids = [str(uuid.uuid4()) for _ in documents]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )
    return len(documents)


def search_documents(question, documents=None, top_k=5):
    if documents:
        add_documents(documents)

    if collection.count() == 0:
        return []

    model = get_model()
    query_embedding = model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(top_k, collection.count())
    )

    return results["documents"][0]
