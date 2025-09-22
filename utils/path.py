from pathlib import Path

def normalize_path(p: Path) -> str:
    return str(p.resolve().as_posix())
