import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# background="..." doesn't work...
ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
ttk.Style().configure('green/black.TButton', foreground='green', background='black')
label = ttk.Label(root, text='I am a ttk.Label with text!', style='black/black.TLabel')
label.pack()
button = ttk.Button(root, text='Click Me!', style='black/black.TButton')
button.pack()
button = tk.Button(root, text='Clicka  Me!')
button.pack()
root.mainloop()
