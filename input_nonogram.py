
from tkinter import *
from process_nonogram import *
from tkinter import messagebox
fields = ('# Rows', '# Columns', 'Row Constraints',
          'Column Constraints', "File Name")


def extract_nonogram_info(entries):

    # get info from nonogram
    n_rows = int(entries["# Rows"].get())
    n_columns = int(entries["# Columns"].get())
    row_constraints = entries["Row Constraints"].get().split("|")
    column_constraints = entries["Column Constraints"].get().split("|")
    file_name = entries["File Name"].get()

    if n_rows != len(row_constraints):
        messagebox.showinfo("Error", "# of rows doesn't match input.")
    if n_columns != len(column_constraints):
        messagebox.showinfo("Error", "# of columns doesn't match input.")

    # create the nonogram file and then parse and process it
    create_nonogram_file(row_constraints, column_constraints, file_name)
    nonogram = nonogram_parse(file_name)
    solve_nonogram(nonogram)


def create_nonogram_file(row_constraints, column_constraints,
                         file_name):

    with open(file_name, "w") as f:
        f.write("H\n")
        for cons in row_constraints:
            f.write(cons + "\n")
        f.write("V\n")
        for cons in column_constraints:
            f.write(cons + "\n")

    messagebox.showinfo("Success!", "The Nonogram info was outputted" +
                        "to " + file_name + ".")


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Generate Nonogram")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: extract_nonogram_info(e)))
    b1 = Button(root, text='Generate',
                command=(lambda e=ents: extract_nonogram_info(e)))
    b1.pack(side=LEFT, padx=35, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=RIGHT, padx=35, pady=5)
    root.mainloop()
