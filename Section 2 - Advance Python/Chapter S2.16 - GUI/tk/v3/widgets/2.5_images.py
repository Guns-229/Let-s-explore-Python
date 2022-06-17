import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

def changephoto():
   tmpimgpath = filedialog.askopenfilename(initialdir=os.getcwd())
   selectedpicture = ImageTk.PhotoImage(file=tmpimgpath)
   PictureLabel= tk.Label(root, width=300, height=400)
   PictureLabel.pack()
   PictureLabel.configure(image=selectedpicture)

root = tk.Tk()
changephoto()
root.mainloop()
