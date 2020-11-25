#!/usr/bin/env python3
import sys
from tail.core import Tail

def parse_arguments():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-f':
        return (True, args[1])
    elif len(args) == 1:
        return (False, args[0])
    else:
        raise RuntimeError('Usage: tail <-f> <filename>') 

def main():
    try:
        is_follow, filename = parse_arguments()
        with open(filename) as fh:
            tail = Tail(fh)
            for line in tail.get_last_lines():
                print(line, end='')
            if is_follow:
                for line in tail.follow():
                    print(line, end='')
    except FileNotFoundError:
        print(f"tail: {filename}: No such file or directory")
        exit(1)
    except RuntimeError:
        print("Usage: tail <-f> <filename>")
        exit(1)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
