import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()

def PrintMsg():
    val = fd.askopenfilename()
    print(val)
    val = fd.askopenfilename(pattern="*.html")
    val = fd.askdirectory()
    print(val)


tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed", 
         fg="light blue",
         bg="Dark blue").pack()

tk.Button(root, text="Next", command=PrintMsg).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()


