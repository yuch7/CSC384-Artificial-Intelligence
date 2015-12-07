from cspbase import *
import sys

def nonogram_csp(c):
	"""
    Return a CSP object representing a nonogram CSP problem along with
    an array of Variables for the problem. That is, return

    nonogram_csp, variable_array
    """

 	lcsp = []
	board = []
	for i in range(len(c[0])):
		board.append([])
		for j in range(len(c[1])):
			board.append([])
			newvar = Variable("{}{}".format(i, j), [0,1])
			board[i][j] = newvar
			lscp.append(newvar)

	nonogram_csp = CSP("Nonogram", lcsp)

	for i in range(len(c[0])):
		for j in range(len(i)):
			sat_tuples = []
			l = sum(c[0][i][:j]) + len(c[0][i][:j])
			r = sum(c[0][i][j+1:]) + len(c[0][i][j+1:])
			var = board[i][l:-r]
			sat_tuples = get_sat_tuples(len(var), c[0][i][j])
			c = Constraint("row{} consecutive: {}".format(i, c[0][i][j]), var)
		    c.add_satisfying_tuples(sat_tuples)
		    nonogram_csp.add_constraint(c)

	for i in range(len(c[1])):
		for j in range(len(i)):
			sat_tuples = []
			l = sum(c[1][:i][j]) + len(c[1][i][:j])
			r = sum(c[1][i][j+1:]) + len(c[1][i][j+1:])
			var = [ w[j] for w in board[l:-r]]
			sat_tuples = get_sat_tuples(len(var), c[1][i][j])
			c = Constraint("col{} consecutive: {}".format(i, c[1][i][j]), var)
		    c.add_satisfying_tuples(sat_tuples)
		    nonogram_csp.add_constraint(c)

    return nonogram_csp, board

def get_sat_tuples(space, num):
	sat = []
	if (space == num):
		return [ 1 for x in range(num)]
	if (space < num):
		print("Error! Invalid file.")
		sys.exit()
	for i in range(space - num + 1):
		sat.append(get_sat_tuple_help(space, num, i))
	return sat

def get_sat_tuple_help(space, num, index):
	sat = []
	count = 0
	for i in range(space):
		if (count == num):
			sat.append(0)
		else:
			if (i >= index):
				sat.append(1)
				count++
			else:
				sat.append(0)
	return sat


def nonogram_parse(filename):
	"""
	Return horizontal and vertical raw constraints 
	"""
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