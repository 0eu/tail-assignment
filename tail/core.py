from time import sleep


class Tail:
    LINES_LIMIT = 10
    SEEK_FILE_END = 2
    LINE_BREAKER = '\n'
    POLLING_INTERVAL = 0.1

    def __init__(self, file_handler):
        self._file_handler = file_handler

    def get_last_lines(self):
        """
            Returns last rows limted by LINES_LIMIT. 
        """
        self._move_to_tail()
        lines = self._get_lines_offset_and_length()
        for offset, length in reversed(lines):
            line = self._read_at(offset, length)
            if len(line) != 0: 
                yield line 

    def _move_to_tail(self):
        """
            Seek to the end of a file.
        """
        self._file_handler.seek(0, Tail.SEEK_FILE_END)


    def _get_lines_offset_and_length(self):
        """
            Collect a start offset for each line:
            Read from the end of a file until there are less than LINES_COUNT offsets
            or nothing to read more.
        """
        current_lines_offsets = [] 
        current_line_length = 1 
        for offset in range(self._file_handler.tell(), -1, -1):
            current_char = self._read_at(offset, 1) 
            if current_char == Tail.LINE_BREAKER:
               current_lines_offsets.append((offset+1, current_line_length))
               current_line_length = 1
            else:
                current_line_length += 1
            if len(current_lines_offsets) - 1 == Tail.LINES_LIMIT:
                break
        else:
            if current_line_length > 1:
                current_lines_offsets.append((offset, current_line_length))
        return current_lines_offsets

    def _read_at(self, offset, buffer_size):
        """
            Return a string with given buffer size from an offset.
        """
        self._file_handler.seek(offset)
        return self._file_handler.read(buffer_size)

    def follow(self):
        """
            Follow the tail. It works as a tail utility: prints all the appended lines.
        """
        self._move_to_tail()
        while True:
            line = self._file_handler.readline()
            if not line:
                sleep(Tail.POLLING_INTERVAL)
                continue
            yield line
