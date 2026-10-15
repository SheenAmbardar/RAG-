
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sentinel.agents.workflow import research_app

documents = [
    "ChromaDB stores and searches vector embeddings.",
    "Sentence Transformers creates text embeddings.",
    "Retrieval augmented generation uses retrieved context to help answer questions."
]

result = research_app.invoke({
    "question": "What does ChromaDB do?",
    "documents": documents,
    "evidence": [],
    "answer": "",
    "verification": {}
})

print("\nANSWER:")
print(result["answer"])

print("\nRETRIEVED EVIDENCE:")
for passage in result["evidence"]:
    print("-", passage)

print("\nVERIFICATION:")
print(result["verification"])
