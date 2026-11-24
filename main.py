"""make.fun round-2 program: "One Letter: Coffee or Tea".

Answer: B — tea. The judge brief scores A for coffee and B for tea,
and anything else loses to any A/B letter, so the entry must be B
(round 1 already used A). The file /output/entry.txt holds just B.

Deterministic by design: standard library only, no network access,
no time, no randomness.
"""

from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
ANSWER = "B"


def _clear_output_contents() -> None:
    """Empty /output without ever removing the /output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for entry in OUTPUT_DIR.iterdir():
        if entry.is_file() or entry.is_symlink():
            entry.unlink()


def _check_written_answer() -> None:
    """Read the file back and fail loudly unless it is exactly 'B'."""
    written = OUTPUT_FILE.read_bytes()
    if written != b"B":
        raise ValueError(f"entry.txt must be exactly one byte 'B', got {written!r}")


def build_entry() -> None:
    _clear_output_contents()
    OUTPUT_FILE.write_bytes(ANSWER.encode("ascii"))
    OUTPUT_FILE.chmod(0o644)
    _check_written_answer()


if __name__ == "__main__":
    build_entry()
