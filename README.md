# Tail
A simple implementation of UNIX tail utility. It prints the last lines of a given file. Also, it can be used with *-f* option to follow new lines or/and *-n* option to specify the number of lines to print. 

## Implementation
Seek to the end of a file and count the number of line breakers. If there are a sufficient amount of lines to print, it breaks the loop and starts to yield lines. Whereas if the required number of lines to print is more than a file has an algorithm seeks to the file's beginning and yield lines from there. 
In case, there is a *-f* option is specified, the two parts will be chained: print the last N lines of a file, and follow the new lines. For the sake of brevity and performance, there are used generators. 

## How to run it?
Make it executable with:
```bash
chmod +x tail.py
```
Run:
```bash
./tail.py <path_to_file>
```

## How to test follow mode?
Start to generate and append new lines to the file: *tests/test_data/logs_stream.log*:
```bash
make generate
```
Run an utility with `-f` option:
```bash
./tail.py -f tests/test_data/logs_stream.log
```

## Tests
There are a couple of tests that were written during development:
```bash
make test
```

## Further Improvements
- Write a test for following the tail.
- Read to a buffer more than one character.
