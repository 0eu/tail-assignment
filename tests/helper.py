def return_rows_list(filename, Tail):
    with open(filename) as fh:
        tail = Tail(fh)
        return list(line for line in tail.get_last_lines()) 
