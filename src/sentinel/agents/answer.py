
def generate_answer(question, passages):
    if not passages:
        return {
            "answer": "I could not find relevant evidence in the indexed documents.",
            "sources": []
        }

    sources = [
        {"id": i + 1, "text": text}
        for i, text in enumerate(passages)
    ]

    answer = (
        "Based on the retrieved documents, here is the available evidence. "
        "Review the cited passages below before treating this as a verified fact."
    )

    return {
        "answer": answer,
        "sources": sources
    }
