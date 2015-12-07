from tkinter import Tk, Canvas


class Display(Tk):

    def __init__(self, board, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        canvas_width = 600
        canvas_height = 600

        divide =
        self.canvas = Canvas(
            self, width=canvas_width, height=canvas_height,
            borderwidth=0, highlightthickness=0)
        self.title("Nonogram Display")
        self.canvas.pack(side="top", fill="both", expand="true")

        # dynamically create the different lengths for rows and columns
        self.rows = len(board)
        self.columns = len(board[0])
        self.cell_width = canvas_width / self.columns
        self.cell_height = canvas_height / self.rows

        self.rect = {}
        self.oval = {}

        # generate the visual board by iterating over board
        for column in range(len(board[0])):
            for row in range(len(board)):

                x1 = column * self.cell_width
                y1 = row * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                # set the tile to black if it's a solution tile
                if board[row][column] == 1:
                    self.rect[row, column] = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="black", tags="rect")
                else:
                    self.rect[row, column] = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="white", tags="rect")


def determine_max_square_size(n_rows, n_columns):
    """
    Given an m x n rectangle, we need to fill it with k squares.
    The function determines the optimal size (largest) that can fit
    into the rectangle.
    """
    h = 1
    w = 1
    max_squares = 1
    size = min(n_rows, n_columns)
    while (n_rows * n_columns) > max_squares:
        if n_rows / (h + 1) >= n_columns / (w + 1):
            h += 1
        else:
            w += 1
        max_squares = h * w
        size = min(n_rows / h, n_columns / w)

    return size


def display_board(board):
    """
    Takes in a final nonogram board, and creates the visual
    representation of the board using Display. A value of one inside
    of our nonogram representation means that the associated
    tile is colored.

    board: a list of lists

    example:
    >>> display_board([[0, 1, 0], [1, 1, 0], [1, 0, 0]])

    """
    app = Display(board)
    app.mainloop()

# print(determine_max_square_size(100, 100))
display_board([[0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 0, 1]])
