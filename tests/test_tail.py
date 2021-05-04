import pytest
from tail import read_last_lines, follow_lines


@pytest.mark.parametrize("file_,expected", [
    ("tests/test_data/empty.log", []), 
    ("tests/test_data/empty_lines.log", ['\n'] * 10), 
    ("tests/test_data/short.log", ['1\n', 'a\n']),
    ("tests/test_data/numbers.log", ['6\n', '7\n', '\n', '\n', '8\n', '\n', '9\n', '10\n', '\n', '11\n'])
])
def test_input_various_length(file_, expected):
    with open(file_, 'r') as fh:
        actual = list(read_last_lines(fh)) 
        assert actual == expected 
