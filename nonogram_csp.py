from cspbase import *
import sys


def nonogram_csp_model(initial_board):
    """
    Return a CSP object representing a nonogram CSP problem along with
    an array of Variables for the problem. That is, return

    nonogram_csp, variable_array
    """

    lcsp = []
    board = []
    for i in range(len(initial_board[0])):
        board.append([])
        for j in range(len(initial_board[1])):
            board[i].append([])
            newvar = Variable("{}{}".format(i, j), [0, 1])
            board[i][j] = newvar
            lcsp.append(newvar)

    nonogram_csp = CSP("Nonogram", lcsp)

    for i in range(len(initial_board[0])):
        for j in range(len(initial_board[0][i])):
            sat_tuples = []
            l = sum(initial_board[0][i][:j]) + len(initial_board[0][i][:j])
            r = sum(initial_board[0][i][j+1:]) + len(initial_board[0][i][j+1:])
            if r == 0:
                var = board[i][l:]
            else:
                var = board[i][l:-r]
            sat_tuples = get_sat_tuples(len(var), initial_board[0][i][j])
            # print(var)
            # print(sat_tuples)
            c = Constraint("row{} consecutive: {}".format(i, initial_board[0][i][j]), var)
            c.add_satisfying_tuples(sat_tuples)
            nonogram_csp.add_constraint(c)

    for i in range(len(initial_board[1])):
        for j in range(len(initial_board[1][i])):
            sat_tuples = []
            l = sum(initial_board[1][i][:j]) + len(initial_board[1][i][:j])
            r = sum(initial_board[1][i][j+1:]) + len(initial_board[1][i][j+1:])
            if r == 0:
                var = [ w[i] for w in board[l:] ]
            else:    
                var = [ w[i] for w in board[l:-r] ]
            sat_tuples = get_sat_tuples(len(var), initial_board[1][i][j])
            # print(var)
            # print(sat_tuples)
            c = Constraint("col{} consecutive: {}".format(i, initial_board[1][i][j]), var)
            c.add_satisfying_tuples(sat_tuples)
            nonogram_csp.add_constraint(c)


    return nonogram_csp, board


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
        check = f.readline()
        if check.strip() != "H":
            print("Invalid file")
            sys.exit()
        for line in f:
            line = line.strip()
            if line == "V":
                break
            rows.append([int(n) for n in line.split()])
        for line in f:
            line = line.strip()
            columns.append([int(n) for n in line.split()])

    return (rows, columns)

def get_sat_tuples(space, num):
    sat = []
    if (space == num):
        return [[1 for x in range(num)]]
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
                count += 1
            else:
                sat.append(0)
    return sat

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 nonogram_csp <filename>")
        sys.exit()

    nonogram_name = sys.argv[1]
    nonogram_parse(nonogram_name)
