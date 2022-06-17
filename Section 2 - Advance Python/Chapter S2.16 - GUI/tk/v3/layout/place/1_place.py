import tkinter as tk

app = tk.Tk()

app.geometry('300x200')
label_top = tk.Button(app, text="Top Side")
label_top.place(x=100, y=10)
label_bottom = tk.Button(app, text="bottom side")
label_bottom.place(x=100, y=150)
label_left = tk.Button(app, text="Left side")
label_left.place(x=10, y=100)
label_right = tk.Button(app, text="Right side")
label_right.place(x=100, y=100)
app.mainloop()
