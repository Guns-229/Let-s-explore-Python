import tkinter as tk

## NEVER DO THIS, BAD IDEA
## from tkinter import *

root = tk.Tk()
root.title('pack Sample 1')
tk.Button(root, text="Hello 1").pack(fill=tk.BOTH)
tk.Button(root, text="Hello R 1").pack(fill=tk.X)
tk.Button(root, text="Hello Both").pack(side='left', fill=tk.BOTH)

tk.mainloop()
