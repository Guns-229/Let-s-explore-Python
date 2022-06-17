from tkinter import *
from PIL import ImageTk, Image

root = Tk()
canv = Canvas(root, width=480, height=480, bg='white')
canv.pack()
img = ImageTk.PhotoImage(Image.open("../files/2.png"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)
mainloop()
