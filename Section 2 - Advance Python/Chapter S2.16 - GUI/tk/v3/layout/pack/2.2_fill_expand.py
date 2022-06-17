import tkinter as tk

root = tk.Tk()

tk.Button(root, text="Hello 1").pack(fill=tk.X)
tk.Button(root, text="Hello L 1" ).pack(fill=tk.BOTH, expand=True)

tk.mainloop()
