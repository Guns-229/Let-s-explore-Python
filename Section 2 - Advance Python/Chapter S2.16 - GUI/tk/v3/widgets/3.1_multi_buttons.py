import tkinter as tk

root = tk.Tk()

def PrintMsg():
    print("Welcome to mayaworld")

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed",
         fg="light blue",
         bg="Dark blue").pack()

tk.Button(root, text="Next", command=PrintMsg).pack()
tk.Button(root, text="Quit", command=root.destroy).pack()

root.mainloop()


