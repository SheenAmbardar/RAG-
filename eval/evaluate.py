
def evaluate_retrieval(retrieved, relevant):
    retrieved = set(retrieved)
    relevant = set(relevant)

    if not retrieved or not relevant:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0
        }

    true_positive = len(retrieved & relevant)

    precision = true_positive / len(retrieved)
    recall = true_positive / len(relevant)

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall else 0.0
    )

    return {
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3)
    }


if __name__ == "__main__":
    retrieved = ["doc1", "doc2", "doc3"]
    relevant = ["doc1", "doc3", "doc4"]

    print("Retrieval Evaluation")
    print(evaluate_retrieval(retrieved, relevant))
