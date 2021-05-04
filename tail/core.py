import os
from typing import Generator, TextIO

BUFFER_SIZE = 1
LINE_BREAK_CHAR = "\n"


def read_last_lines(fh: TextIO, lines: int = 10) -> Generator[str, None, None]:
    fh.seek(0, os.SEEK_END)
    found_lines = 0

    for offset in range(fh.tell() - 1, -1, -1):
        fh.seek(offset)
        if fh.read(BUFFER_SIZE) == LINE_BREAK_CHAR:
            found_lines += 1

        if found_lines > lines:
            break

    if found_lines <= lines:
        fh.seek(0)

    while (line := fh.readline()) and line and found_lines > 0:
        yield line
        found_lines -= 1


def follow_lines(fh: TextIO) -> Generator[str, None, None]:
    while True:
        yield from fh.readlines()