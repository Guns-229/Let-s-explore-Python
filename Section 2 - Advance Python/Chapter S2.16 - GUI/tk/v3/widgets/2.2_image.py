"""
As the canvas is smaller than the image
it will display only partial image.
"""
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
canv = Canvas(root, width=280, height=280, bg='white')
canv.pack()
img = ImageTk.PhotoImage(Image.open("../files/2.jpg"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)
mainloop()
