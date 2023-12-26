#!/usr/bin/env python3

# Standard libraries.
import collections.abc as cabc
import contextlib
import sys


@contextlib.contextmanager
def print_exception() -> cabc.Iterator[None]:
    try:
        yield
    except Exception as error:
        print("Exception passthrough:", error)
        raise


def preload() -> None:
    module_paths = ("pyxel_how/__init__.py", "pyxel_how/hello.py")
    for path in module_paths:
        with open(path):  # pylint: disable=unspecified-encoding
            pass


@print_exception()
def main() -> int:
    preload()
    import pyxel_how.hello  # type: ignore[import-not-found] # pylint: disable=import-error,import-outside-toplevel

    return pyxel_how.hello.main()  # type: ignore[no-any-return]


if __name__ == "__main__":
    sys.exit(main())
