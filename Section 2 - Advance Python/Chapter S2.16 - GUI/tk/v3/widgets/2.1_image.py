from tkinter import *
root = Tk()

canv = Canvas(root, width=80, height=80, bg='white')
canv.pack()
img = PhotoImage(file="../files/2.jpg")  # WE cannot add images directly to the PhotoImage
canv.create_image(20,20, anchor=NW, image=img)

mainloop()
