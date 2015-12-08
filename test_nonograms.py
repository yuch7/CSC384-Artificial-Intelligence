from process_nonogram import *


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

    total = 0
    goal = len(files)

    for text in files:
        print('Testing ' + text + " ...")
        if (text == 'nono1.txt'):
            solution = [[1, 1, 1, 0, 0],[1, 1, 1, 0, 0],[1, 0, 1, 0, 0],[0, 0, 1, 0, 1],[0, 1, 0, 1, 1]]
            total = total + test(text, solution)
        elif (text == 'nono3.txt'):
            solution = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],[0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            total = total + test(text, solution)
        elif (text == 'nono4.txt'):
            solution = [[0, 0, 0, 0, 1, 0, 1, 1, 1, 1],[0, 0, 0, 0, 1, 1, 1, 1, 1, 1],[0, 0, 0, 1, 1, 1, 1, 1, 1, 0],[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],[1, 1, 1, 1, 1, 1, 0, 0, 0, 1],[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 1, 1, 1, 1, 1, 0, 1, 0],[0, 0, 0, 1, 1, 1, 0, 1, 1, 0],[0, 0, 0, 1, 0, 0, 0, 1, 1, 0]]
            total = total + test(text, solution)
        elif (text == 'nono5.txt'):
            solution = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 1],[0, 0, 0, 0, 0, 1, 1, 0, 1, 1],[0, 1, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],[0, 0, 0, 1, 0, 0, 0, 0, 1, 1],[1, 1, 1, 0, 1, 1, 1, 1, 1, 0],[1, 1, 1, 0, 1, 1, 1, 1, 0, 0],[1, 1, 1, 1, 1, 0, 1, 1, 0, 0],[1, 1, 1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
            total = total + test(text, solution)
        elif (text == 'nono6.txt'):
            solution = [[1, 1, 1, 1, 0],[1, 1, 1, 0, 0],[1, 1, 0, 0, 0],[0, 0, 0, 1, 0],[0, 0, 1, 1, 1]]
            total = total + test(text, solution)
        else:
            instance = nonogram_parse(text)
            solve_nonogram(instance, True)

    print(str(total) + ' tests passed out of ' + str(goal))

def test(fname, solution):
    instance = nonogram_parse(fname)
    result = solve_nonogram(instance, False)
    c_rows = 0
    for row in result:
        if tuple(solution[0]) != tuple(row):
            print("Test Failed :(")
            print(tuple(row))
            print(list(solution))
            return 0
        else: c_rows = c_rows + 1
        solution.pop(0)
    if(c_rows == len(result)):
        print('Test Passed!')
        return 1

if __name__ == "__main__":

    test_file = "full_test.txt"
    test_nonograms(test_file)
