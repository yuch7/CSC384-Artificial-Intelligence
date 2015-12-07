from cspbase import *
import sys


def nonogram_csp_model(initial_board):
    """
    Return a CSP object representing a nonogram CSP problem along with
    an array of Variables for the problem. That is, return

    nonogram_csp, variable_array
    """

    nonogram_csp, variable_array = construct_base_csp(initial_board)

    for row in varialbe_array:
        pass

    transpose = list(map(list, zip(*variable_array)))
    for row in transpose:
        pass

    return (nonogram_csp, variable_array)


def nonogram_parse(filename):
    """
    Take a specific filename as input, and then parse the
    file in order to produce an initial nonogram form. Assumes
    that the file is a valid nonogram file.

    Returns a tuple of the form (list, list).
    """
    rows = []
    columns = []

    with open(filename) as f:

        for line in f:
            rows.append(line.split())
            if line == "V":
                break
        for line in f:
            columns.append(line.split())

    return (rows, columns)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 nonogram_csp <filename>")
        sys.exit()

    nonogram_name = sys.argv[1]
    nonogram_parse(nonogram_name)
    # TODO: solve
