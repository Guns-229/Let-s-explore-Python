import tkinter as tk

root = tk.Tk()

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed", 
         fg="light blue",
         bg="Dark blue").pack()

tk.Button(root, text="Next", width=20).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
