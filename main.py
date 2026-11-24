"""Round-2 entry for "One Letter: Coffee or Tea" (make.fun).

The program answers with a single letter: C, for coffee.
It writes that letter and nothing else to /output/entry.txt.

No network, no clock, no randomness, Python standard library only,
so every run produces the same single byte.
"""

from pathlib import Path

ENTRY = Path("/output/entry.txt")
CHOICE = "C"


def _empty_output_dir() -> None:
    """Remove the contents of /output, never the directory itself."""
    ENTRY.parent.mkdir(parents=True, exist_ok=True)
    for item in ENTRY.parent.iterdir():
        if item.is_symlink() or item.is_file():
            item.unlink()


def _guard_written_text() -> None:
    """Confirm the file on disk is exactly one non-whitespace character."""
    text = ENTRY.read_text(encoding="utf-8")
    if len(text) != 1 or text.isspace():
        raise ValueError("entry.txt must hold exactly one non-whitespace letter")


def run() -> None:
    _empty_output_dir()
    ENTRY.write_text(CHOICE, encoding="utf-8")
    ENTRY.chmod(0o644)
    _guard_written_text()


if __name__ == "__main__":
    run()
