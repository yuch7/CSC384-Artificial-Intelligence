from propagators import *
from nonogram_csp import *


def solve_nonogram(nonograms):

    for nono in nonograms:
        print("Using nonogram model:")
        csp, var_array = nonogram_csp_model(nono)
        solver = BT(csp)
        print("=======================================================")
        print("GAC")
        solver.bt_search(prop_GAC)
        print("Solution")
        print_sudo_soln(var_array)


def test_nonograms(test_file):
    """
    Takes a file containing the name of a nonogram files
    per line, and then creates and solves instances of those
    nonograms.
    """

    files = []
    with open(test_file) as f:
        for line in f:
            files.append(line.strip())

    for text in files:
        instance = nonogram_parse(text)
        solve_nonogram(instance)

if __name__ == "__main__":

    test_file = "full_test.txt"
    test_nonograms(test_file)
