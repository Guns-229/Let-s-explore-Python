import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()

def PrintMsg():
    val = mb.askokcancel(title="Proceed", message="Do you wish to proceed")
    print(val)

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed",
         fg="light blue",
         bg="Dark blue").pack()

tk.Button(root, text="Next", command=PrintMsg).pack()
tk.Button(root, text="Quit", command=root.destroy,
          highlightbackground ="#8EF0F7", pady=2,
          relief=tk.FLAT).pack()

root.mainloop()
