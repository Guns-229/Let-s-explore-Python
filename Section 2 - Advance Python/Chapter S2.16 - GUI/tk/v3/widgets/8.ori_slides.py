import tkinter as tk

root = tk.Tk()

vol = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
vol.pack()

tk.mainloop()
