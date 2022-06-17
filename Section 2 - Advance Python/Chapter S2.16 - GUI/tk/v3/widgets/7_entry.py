import tkinter as tk

root = tk.Tk()

def show_name():
    print(name.get())
    name.insert(4, "Thanks")

def clear():
    name.delete(0, 'end')

tk.Label(root, text="Please Enter your name").pack(side=tk.LEFT)
name = tk.Entry(root)
name.insert(0, "Welcome")
name.pack(expand=tk.YES)
tk.Button(root, text="Show name", command=show_name).pack()
tk.Button(root, text="clear", command=clear).pack()
root.mainloop()
