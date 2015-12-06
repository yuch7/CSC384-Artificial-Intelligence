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

if __name__=="__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 nonogram_csp <filename>")
		sys.exit()

	tosolve = open(sys.argv[1], "r")
	line = tosolve.readline()
	if (line != "H"):
		print("Invalid file!")
		sys.exit()
