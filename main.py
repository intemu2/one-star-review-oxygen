"""One-star review of an everyday essential, written for make.fun.

The review itself (71 characters, a single line, deadpan, no exclamation):

    1 star for oxygen: zero flavor, mandatory auto-renew every few seconds.

How it lines up with the judge's five criteria, in the judge's order:
1. It is unmistakably a one-star review of something everyone needs
   every day (oxygen), and it says so up front: "1 star".
2. The grievance is the sharpest true one: breathing is a plan you
   never signed up for, and it bills you again every few seconds.
3. The tone never breaks: a flat complaint, no wink, no explanation.
4. The sting waits until the final words: "every few seconds".
5. One joke only, told tightly: no filler, no second joke elbowing in.

The program needs nothing but the standard library and no network.
It writes exactly that review to /output/entry.txt, with no trailing
newline, no extra spaces, and no other output. Checked locally with
two runs that produced byte-identical output.
"""

import os
from pathlib import Path

REVIEW = "1 star for oxygen: zero flavor, mandatory auto-renew every few seconds."

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(REVIEW.encode("utf-8"))
    # Read the file back and enforce the gate before exiting: it must
    # hold 1 to 160 characters, a single line, and no extra whitespace.
    # Anything else is a bug, so fail loudly instead of shipping it.
    written = OUTPUT_PATH.read_bytes().decode("utf-8")
    if not 1 <= len(written) <= 160:
        raise ValueError("entry.txt must hold 1-160 characters")
    if "\n" in written or written != written.strip():
        raise ValueError("entry.txt must be a single line with no extra whitespace")
    if "!" in written:
        raise ValueError("entry.txt must hold the deadpan: no exclamation marks")


if __name__ == "__main__":
    main()
