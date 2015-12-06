from nonograms import solve_nonogram
from nonograms import parse_nonogram


def test_nonograms(test_file):
    """
    Takes a file containing the name of a nonogram files
    per line, and then creates and solves instances of those
    nonograms.
    """

    files = []
    with open(test_file) as f:
        for line in f:
            files.append(line)

    for text in files:
        instance = parse_nonogram(text)
        solve_nonogram(instance)

if __name__ == "__main__":

    test_file = "full_test.txt"
    test_nonograms(test_file)
