import tkinter as tk

app = tk.Tk()

app.geometry('300x200')
label_top = tk.Button(app, text="Top Side")
label_top.pack(side="top")
label_bottom = tk.Button(app, text="bottom side")
label_bottom.pack(side="bottom")
label_left = tk.Button(app, text="Left side")
label_left.pack(side="left")
label_right = tk.Button(app, text="Right side")
label_right.pack(side="right")
app.mainloop()
