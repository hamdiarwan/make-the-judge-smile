from pathlib import Path

LINE = (
    "At 7:40 this morning the lift repairman got stuck in it with me, "
    "poured me tea from his thermos, and taught me to whistle through an acorn cap; "
    "we both groaned when it started moving."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
