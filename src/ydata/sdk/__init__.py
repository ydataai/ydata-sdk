from pathlib import Path

source_root = Path(__file__).parent

try:
    __version__ = (source_root / "VERSION").read_text().rstrip("\n")
except FileNotFoundError:
    __version__ = "0.0.dev0"
