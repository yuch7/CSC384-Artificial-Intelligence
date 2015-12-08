from propagators import *
from nonogram_csp import *
from display_nonogram import *


def solve_nonogram(nono, display):
    """
    Take a Nonograph input and generate a model based on the info.
    Then,use backtracking search to solve the CSP. Display the solution
    to a Window with tiles.

    nono: tuple of form (row_constraints, column_constraints)
    """
    print("Using nonogram model:")
    csp, var_array = nonogram_csp_model(nono)
    solver = BT(csp)
    print("=======================================================")
    print("GAC")
    solver.bt_search(prop_GAC)
    board = extract_list(var_array)

    if(display):
        print("Solution")
        print_nonogram_soln(var_array)
        display_board(board)

    return board


def print_nonogram_soln(var_array):
    for row in var_array:
        print([var.get_assigned_value() for var in row])


def extract_list(var_array):
    final = []
    for row in var_array:
        final.append([var.get_assigned_value() for var in row])
    return final


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
