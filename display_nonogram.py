from tkinter import Tk
from tkinter import Canvas


class Display(Tk):

    def __init__(self, board, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        canvas_width = 500
        canvas_height = 500

        self.canvas = Canvas(
            self, width=canvas_width, height=canvas_height,
            borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        self.rows = len(board)
        self.columns = len(board[0])
        self.cell_width = canvas_width / self.rows
        self.cell_height = canvas_height / self.columns

        self.rect = {}
        self.oval = {}
        for column in range(len(board[0])):
            for row in range(len(board)):
                x1 = column * self.cell_width
                y1 = row * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                if board[row][column] == 1:
                    self.rect[row, column] = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="blue", tags="rect")
                else:
                    self.rect[row, column] = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="white", tags="rect")


def display_board(board):
    """
    Takes in a final nonogram board, and creates the visual
    representation of the board using tkinter.

    board: a list of lists
    """
    app = Display(board)
    app.mainloop()


display_board([[0, 1, 0], [1, 1, 0], [1, 0, 0]])
