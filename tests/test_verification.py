
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sentinel.verification.verify import verify_evidence


def test_no_evidence_is_unsupported():
    result = verify_evidence("ChromaDB stores vectors.", [])
    assert result["supported"] is False


def test_matching_evidence_has_overlap():
    result = verify_evidence(
        "ChromaDB stores vectors",
        ["ChromaDB stores vectors"]
    )
    assert result["overlap_score"] > 0


def test_unrelated_evidence_has_low_overlap():
    result = verify_evidence(
        "ChromaDB stores vectors",
        ["Cats enjoy sleeping in sunny places"]
    )
    assert result["supported"] is False
