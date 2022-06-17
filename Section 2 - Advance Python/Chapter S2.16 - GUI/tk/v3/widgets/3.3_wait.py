import tkinter as tk
from time import sleep

def PrintMsg():
    print("Welcome to mayaworld")
    sleep(5)

root = tk.Tk()

mFrame = tk.Frame(root)
mFrame.pack()


tk.Label(mFrame, text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed",
         fg="light blue",
         bg="Dark blue").pack()

tk.Button(mFrame, text="Next", command=PrintMsg).pack()
tk.Button(mFrame, text="Quit", command=root.destroy).pack()

root.mainloop()


