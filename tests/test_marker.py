from pathlib import Path

def test_marker_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "app" / "README_marker.txt").exists()
