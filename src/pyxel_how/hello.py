#!/usr/bin/env python3

# Standard libraries.
import sys

# External libraries.
import pyxel


def main() -> int:
    pyxel.init(160, 120, title="Hello Pyxel")

    def update() -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw() -> None:
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)

    pyxel.run(update, draw)
    return 0


if __name__ == "__main__":
    sys.exit(main())
