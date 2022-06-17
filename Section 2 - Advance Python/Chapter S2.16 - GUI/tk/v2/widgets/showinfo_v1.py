import Tkinter as tk
import tkMessageBox

def showMessage(title, msg):
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    tkMessageBox.showinfo(title, msg, parent=root)

showMessage("Title", "This is message")
