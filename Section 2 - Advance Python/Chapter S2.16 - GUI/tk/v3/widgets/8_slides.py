import tkinter as tk

root = tk.Tk()

def get_vals():
    print(vol.get())

vol = tk.Scale(root, from_=0, to=100)
vol.pack()
vol.set(10)

tk.Button(root, text="Get Vol" command=get_vals).pack()
tk.mainloop()
