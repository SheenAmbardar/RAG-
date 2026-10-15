
import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sentinel.agents.workflow import research_app

st.set_page_config(
    page_title="Sentinel Research AI",
    page_icon="🔎",
    layout="wide"
)

st.title("Sentinel — Research Intelligence")
st.caption("Semantic retrieval • Local LLM • Evidence verification")

uploaded = st.file_uploader(
    "Upload a research document",
    type=["txt"]
)

question = st.text_area("Research question")

if st.button("Run Research", type="primary"):
    if uploaded is None or not question.strip():
        st.warning("Upload a TXT document and enter a question.")
    else:
        text = uploaded.getvalue().decode("utf-8", errors="replace")
        documents = [p.strip() for p in text.splitlines() if p.strip()]

        try:
            with st.spinner("Retrieving evidence and generating answer..."):
                result = research_app.invoke({
                    "question": question,
                    "documents": documents,
                    "evidence": [],
                    "answer": "",
                    "verification": {}
                })

            st.subheader("Research Answer")
            st.write(result["answer"])

            st.subheader("Evidence Verification")
            verification = result["verification"]
            st.write("Supported by overlap heuristic:", verification["supported"])
            st.write("Overlap score:", verification.get("overlap_score", 0))
            st.caption(verification["reason"])

            st.subheader("Retrieved Sources")
            for i, passage in enumerate(result["evidence"], 1):
                with st.expander(f"Source [{i}]"):
                    st.write(passage)

        except Exception as error:
            st.error(f"Research failed: {error}")
            st.info(
                "Check that Ollama is installed, the model is downloaded, "
                "and the embedding model is available."
            )
