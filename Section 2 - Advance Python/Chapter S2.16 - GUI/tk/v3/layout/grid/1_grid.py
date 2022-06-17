import tkinter as tk

root = tk.Tk()

states = {"mp": "bpl", "ap": "hyd", "ka": "Bangaluru"}

row = 0

for key, val in states.items():
    tk.Label(text=key, relief=tk.RIDGE, width=20).grid(row=row, column=0)
    tk.Label(text=val, relief=tk.RIDGE, width=20).grid(row=row, column=1)
    row +=1

tk.mainloop()

