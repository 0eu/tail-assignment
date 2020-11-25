import unittest
from tail.core import Tail
from tests.helper import return_rows_list


class TestTail(unittest.TestCase):
    def test_empty_file(self):
        filename = 'tests/test_data/empty.log'
        actual = return_rows_list(filename, Tail)
        expected = []
        self.assertEqual(actual, expected) 
        self.assertEqual(len(actual), len(expected)) 

    def test_empty_lines_file(self):
        filename = 'tests/test_data/empty_lines.log'
        actual = return_rows_list(filename, Tail)
        expected = ['\n'] * 10
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected)) 

    def test_dotted_file(self):
        filename = 'tests/test_data/dotted.log'
        actual = return_rows_list(filename, Tail)
        expected = ['.\n', '\n', '.\n', '\n', '.\n', '\n', '\n', '.\n', '\n']
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected)) 

    def test_short_file(self):
        filename = 'tests/test_data/short.log'
        actual = return_rows_list(filename, Tail)
        expected = ['1\n', 'a\n']
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected)) 

    def test_numbers_file(self):
        filename = 'tests/test_data/numbers.log'
        actual = return_rows_list(filename, Tail)
        expected = ['6\n', '7\n', '\n', '\n', '8\n', '\n', '9\n', '10\n', '\n', '11\n']
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected)) 

if __name__ == '__main__':
    unittest.main()
