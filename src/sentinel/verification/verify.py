
def verify_evidence(answer, passages):
    if not passages:
        return {
            "supported": False,
            "reason": "No evidence found."
        }

    answer_words = set(answer.lower().split())
    evidence_text = " ".join(passages).lower()
    evidence_words = set(evidence_text.split())

    common = answer_words.intersection(evidence_words)
    score = len(common) / max(len(answer_words), 1)

    return {
        "supported": score >= 0.25,
        "overlap_score": round(score, 2),
        "reason": (
            "Some answer words match the evidence."
            if score >= 0.25
            else "Evidence overlap is low; review the answer."
        )
    }
