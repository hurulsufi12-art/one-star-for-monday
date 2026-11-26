#!/usr/bin/env python3
"""One Star for Monday.

Writes a one-star review of Monday, written as if Monday were a
restaurant, to /output/entry.txt. Stdlib only, deterministic, no
network, no model.
"""
import os
import sys

MAX_CHARS = 180
MAX_WORDS = 25


class MondayReview:
    """The single review line, held as class data with its own checks."""

    VERDICT = "One star."
    SEATING = "Monday seated us at 6 a.m.,"
    DISH = "served cold coffee,"
    BILL = "charged full price for the weekend,"
    PUNCHLINE = "and the waiter was also Monday."

    @classmethod
    def render(cls):
        return " ".join([cls.VERDICT, cls.SEATING, cls.DISH,
                         cls.BILL, cls.PUNCHLINE])

    @classmethod
    def validate_review(cls, text):
        """Raise ValueError if the text breaks any sealed gate."""
        if not isinstance(text, str):
            raise ValueError("entry must be text")
        if not text.strip():
            raise ValueError("entry must not be only whitespace")
        if "\n" in text or "\r" in text:
            raise ValueError("entry must be a single line")
        if len(text) > MAX_CHARS:
            raise ValueError("entry is %d chars, over the %d limit"
                             % (len(text), MAX_CHARS))
        if len(text.split()) > MAX_WORDS:
            raise ValueError("entry is %d words, over the %d limit"
                             % (len(text.split()), MAX_WORDS))
        text.encode("utf-8")  # raises if not encodable as UTF-8


def main():
    text = MondayReview.render()
    try:
        MondayReview.validate_review(text)
    except ValueError as exc:
        print("gate failed: %s" % exc, file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
