from tkinter import Tk, Canvas


def create_board_canvas(board):
    """
    Create a Tkinter Canvas for displaying a Nogogram solution.
    Return an instance of Tk filled as a grid.

    board: list of lists of {0, 1}
    """

    canvas = Tk()
    LARGER_SIZE = 600

    # dynamically set the size of each square based on cols and rows
    n_columns = len(board[0])
    n_rows = len(board)

    divide = max(n_columns, n_rows)
    max_size = LARGER_SIZE / divide
    canvas_width = max_size * n_columns
    canvas_height = max_size * n_rows

    # create the intiial canvas with rows and columns grid
    canvas.canvas = Canvas(
        canvas, width=canvas_width, height=canvas_height,
        borderwidth=0, highlightthickness=0)
    canvas.title("Nonogram Display")
    canvas.canvas.pack(side="top", fill="both", expand="true")

    canvas.rows = len(board)
    canvas.columns = len(board[0])
    canvas.cell_width = max_size
    canvas.cell_height = max_size

    canvas.rect = {}
    canvas.oval = {}

    insert_canvas_grid(canvas, board)

    return canvas


def insert_canvas_grid(canvas, board):
    """
    Insert black and white squares onto a canvas depending on the
    values inside of the board. A value of 1 corresponds to a black
    square, while a value of 0 corresponds to a white squre.

    canvas: Tk object
    board: list of lists of {0, 1}
    """
    # generate the visual board by iterating over board
    for column in range(len(board[0])):
        for row in range(len(board)):

            x1 = column * canvas.cell_width
            y1 = row * canvas.cell_height
            x2 = x1 + canvas.cell_width
            y2 = y1 + canvas.cell_height

            # set the tile to black if it's a solution tile
            if board[row][column] == 1:
                canvas.rect[row, column] = canvas.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="black")
            else:
                canvas.rect[row, column] = canvas.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white")


def display_board(board):
    """
    Takes in a final nonogram board, and creates the visual
    representation of the board using NonogramDisplay.
    A value of one inside of our nonogram representation
    means that the associated tile is colored.

    board: a list of lists (each list is a row)

    example:
    >>> display_board([[0, 1, 0],
                       [1, 1, 0],
                       [1, 0, 0]])

    """
    app = create_board_canvas(board)
    app.mainloop()
