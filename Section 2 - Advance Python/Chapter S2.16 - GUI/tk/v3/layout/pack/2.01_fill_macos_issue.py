import tkinter as tk

app = tk.Tk()
app.geometry('200x200')

tk.Button(app, text="Fills X").pack(fill=tk.X)
tk.Button(app, text="Fills Y").pack(fill='y')

app.mainloop()

