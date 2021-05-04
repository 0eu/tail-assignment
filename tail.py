#!/usr/bin/env python3
from os import path
from itertools import chain
from contextlib import suppress 
from argparse import ArgumentParser 
from tail import read_last_lines, follow_lines


def init_argparse() -> ArgumentParser:
    parser = ArgumentParser(
        usage="tail [-f] [-n number] [FILE]",
        description="The tail utility displays the contents of file to the standard output."
    )
    parser.add_argument("-f", "--follow", action="store_true", default=False)
    parser.add_argument("-n", "--number", type=int, default=10)
    parser.add_argument("FILE", nargs=1, type=readable_file(parser))
    return parser


def readable_file(parser: ArgumentParser):
    def inner(filename: str) -> str:
        if not path.exists(filename):
            parser.error(f"File is not readable: {filename}")
        return filename
    return inner


def tail(filename: str, lines: int, follow: bool):
    with open(filename, "r") as fh:
        lines = read_last_lines(fh, lines)
        if follow:
            lines = chain(lines, follow_lines(fh))
        
        with suppress(KeyboardInterrupt):
            for line in lines:
                print(line, end="")


def main():
    parser = init_argparse()
    args = parser.parse_args()
    tail(
        filename=next(iter(args.FILE)), 
        lines=args.number, 
        follow=args.follow
    )
    

if __name__ == '__main__':
    main()
