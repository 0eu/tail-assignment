# Tail Utility
Simple implementation of unix tail utility. It shows last lines of a file, and also supports following the tail with -f option.

## Implementation
I used a straightforward approach to read last lines of a file: seek to the end of a file and move backward until we reach a line breaker. While iterating, I populate a list with tuple that contains:
- offset: the beginning of a line
- length: actual lenght of a line
After sufficient amount of lines were found, the algorithm iterates the list in reverse order with offsets, read the line  and yields it. Generator was used for the performance purposes. 

### Follow
It will prints last lines of a file and then will await for a new lines. There is a polling interval, I set it to 0.1 second. It waits that time if there weren't new lines appended to a file. If they are it sequentilly read one-by-one and yields it. 

### How to run it?
Make it executable with:
```bash
chmod +x tail_cli.py
```

Now, we are good to run it:
```bash
./tail_cli.py tests/test_data/numbers.log
```

### How to test a follow mode?
Open another tab and execute:
```bash
make generate
```

The command above will start to generate and to append new lines to file: `tests/test_data/logs_stream.log`.

Run an utility with -f flag:
```bash
./tail_cli.py -f tests/test_data/logs_stream.log
```

#### Tests
Also, there are some tests that were written during development. To make them run:
```bash 
make test
```


### Further Improvements
1. More tests.
2. Set up CI with Github Actions.
3. Write more sophisticated algorithm for handling extremely long lines: now we are good until the each single line fits into the memory. We can split up a reading buffer to print out its parts, sequentilly. 
