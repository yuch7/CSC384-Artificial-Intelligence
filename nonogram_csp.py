from cspbase import *
import sys

def nonogram_csp(c):
	board = []
	for i in range(len(c[0])):
		board.append([])
		for j in range(len(c[1])):
			board.append([])
			board[i][j] = Variable("{}{}".format(i, j), [0,1])

 	lcsp = []




def nonogram_parse(filename):
	H = []
	V = []

	tosolve = open(filename, "r")
	line = tosolve.readline()
	print(line)
	if (line != 'H'):
		print("Invalid file!")
		sys.exit()

	while (line != "V"):
		line = tosolve.readline()
		H.append(line.split())
	while (line != ''):
		line = tosolve.readline()
		V.append(line.split())

	tosolve.close()
	return (H, V)