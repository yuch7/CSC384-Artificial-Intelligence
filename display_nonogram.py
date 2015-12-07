from tkinter import Tk, Canvas


class NonogramDisplay(Tk):

    """
    Class used to create instance of a visual nonogram. The class
    creates a new Window and populates a grid with black or white
    squares depending on a nanogram solution.
    """

    LARGER_SIZE = 600

    def __init__(self, board, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        # dynamically set the size of each square based on cols and rows
        n_columns = len(board[0])
        n_rows = len(board)

        divide = max(n_columns, n_rows)
        max_size = self.LARGER_SIZE / divide
        canvas_width = max_size * n_columns
        canvas_height = max_size * n_rows

        # create the intiial canvas with rows and columns grid
        self.canvas = Canvas(
            self, width=canvas_width, height=canvas_height,
            borderwidth=0, highlightthickness=0)
        self.title("Nonogram Display")
        self.canvas.pack(side="top", fill="both", expand="true")

        self.rows = len(board)
        self.columns = len(board[0])
        self.cell_width = max_size
        self.cell_height = max_size

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
                        x1, y1, x2, y2, fill="black")
                else:
                    self.rect[row, column] = self.canvas.create_rectangle(
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
    app = NonogramDisplay(board)
    app.mainloop()

display_board([[0, 1, 0, 1], [1,1, 1, 0], [1, 0, 0, 1]])
