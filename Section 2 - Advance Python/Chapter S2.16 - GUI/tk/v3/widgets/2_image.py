import tkinter as tk

root = tk.Tk()
img = tk.PhotoImage(file="files/2.png")

img_l = tk.Label(root, image=img)
img_l.pack()

root.mainloop()

