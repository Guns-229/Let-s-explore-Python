from tkinter import Tk, BOTH, W, N, E, S, Entry, Label, RIDGE

root = Tk()

states = {"mp": "bpl", "ap": "hyd", "ka": "Bangaluru"}

row = 1

entry = Entry()
entry.grid(row=0, columnspan=4, sticky=W+N)
for key, val in states.items():
    Label(text=key, relief=RIDGE, width=20).grid(row=row, column=0)
    Label(text=val, relief=RIDGE, width=20).grid(row=row, column=1)
    row +=1

root.mainloop()

