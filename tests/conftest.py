import sys
from pathlib import Path


def _add_src_to_syspath() -> None:
    root = Path(__file__).resolve().parents[1]
    src = root
    if src.exists():
        sys.path.insert(0, str(src))


_add_src_to_syspath()