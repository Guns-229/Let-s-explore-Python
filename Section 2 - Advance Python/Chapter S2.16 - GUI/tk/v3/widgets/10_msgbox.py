import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()

def PrintMsg():
    mb.showinfo("OS Selection", "We will be asking question about OS")
    msg = mb.askyesno("OS Question", "Do you use Linux")
    print(msg)
    if not msg:
        mb.showerror("OS Selection", "Sorry cannot proceed")
    else:
        mb.showwarning("OS Selection", "ok, good for you")

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed", 
         fg="light blue",
         bg="Dark blue").pack()

tk.Button(root, text="Next", command=PrintMsg).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()


