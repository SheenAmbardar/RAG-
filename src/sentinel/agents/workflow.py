
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from sentinel.retrieval.search import search_documents
from sentinel.agents.answer import generate_answer
from sentinel.verification.verify import verify_evidence


class ResearchState(TypedDict):
    question: str
    documents: list[str]
    evidence: list[str]
    answer: str
    verification: dict


def retrieve(state: ResearchState):
    evidence = search_documents(
        state["question"],
        state["documents"]
    )
    return {"evidence": evidence}


def answer(state: ResearchState):
    result = generate_answer(
        state["question"],
        state["evidence"]
    )
    return {"answer": result["answer"]}


def verify(state: ResearchState):
    result = verify_evidence(
        state["answer"],
        state["evidence"]
    )
    return {"verification": result}


graph = StateGraph(ResearchState)

graph.add_node("retrieve", retrieve)
graph.add_node("answer", answer)
graph.add_node("verify", verify)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", "verify")
graph.add_edge("verify", END)

research_app = graph.compile()
