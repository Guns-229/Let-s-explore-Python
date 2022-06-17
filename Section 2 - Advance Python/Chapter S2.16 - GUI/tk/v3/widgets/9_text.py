import tkinter as tk

root = tk.Tk()
txtbox = tk.Text(root, height=10)
txtbox.pack(expand=tk.YES, side=tk.LEFT)

tk.Button(root, text="Next", width=20).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
