from cspbase import *
from copy import deepcopy
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

    for i in range(len(board)):
        var = board[i]
        sat_tuples = get_sat_tuples(len(var), initial_board[0][i])
        c = Constraint("row{}".format(i), var)
        c.add_satisfying_tuples(sat_tuples)
        nonogram_csp.add_constraint(c)

    for i in range(len(board[0])):
        var = [ x[i] for x in board ]
        sat_tuples = get_sat_tuples(len(var), initial_board[1][i])
        c = Constraint("col{}".format(i), var)
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

def get_sat_tuples(space, nums, used=[]):
    ret = []
    if (len(nums) == 1):
        for x in range(space - nums[0] + 1):
            used1 = deepcopy(used)
            count = 0
            for y in range(space):
                if (x <= y and count < nums[0]):
                    used1.append(1)
                    count += 1
                else:
                    used1.append(0)
            ret.append(used1)
        return ret
    else:
        tmpspace = space - sum(nums[1:]) + len(nums[1:])
        for x in range(tmpspace - nums[0] + 1):
            used1 = deepcopy(used)
            count = 0
            for y in range(x + nums[0] + 1):
                if (x <= y and count < nums[0]):
                    used1.append(1)
                    count += 1
                else:
                    used1.append(0)
            tmp = get_sat_tuples(space - nums[0] - x - 1, nums[1:], used1)
            for z in tmp:
                ret.append(z)
        return ret

# if __name__ == "__main__":
#     if (len(sys.argv) != 2):
#         print("Usage: python3 nonogram_csp <filename>")
#         sys.exit()

#     nonogram_name = sys.argv[1]
#     nonogram_parse(nonogram_name)