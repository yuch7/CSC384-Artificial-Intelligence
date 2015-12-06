from cspbase import *
import sys

# def nonogram_csp():


if __name__=="__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 nonogram_csp <filename>")
		sys.exit()

	tosolve = open(sys.argv[1], "r")
	line = tosolve.readline()
	if (line != "H"):
		print("Invalid file!")
		sys.exit()