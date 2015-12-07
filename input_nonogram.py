
from tkinter import *
fields = ('# Rows', '# Columns', 'Row Constraints', 'Column Constraints')


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Generate Nonogram")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Generate',
                command=(lambda e=ents: final_balance(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=TOP, padx=5, pady=5)
    root.mainloop()
