from cspbase import *
import sys

def nonogram_csp(initial_board):
    """
    Return a CSP object representing a nonogram CSP problem along with
    an array of Variables for the problem. That is, return

    nonogram_csp, variable_array
    """
    width = len(initial_board[0])
    height = len(intiail_board[1])

if __name__=="__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 nonogram_csp <filename>")
		sys.exit()

	tosolve = open(sys.argv[1], "r")
	line = tosolve.readline()
	if (line != "H"):
		print("Invalid file!")
		sys.exit()
