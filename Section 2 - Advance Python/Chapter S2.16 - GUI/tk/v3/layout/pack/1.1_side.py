import tkinter as tk

app = tk.Tk()

app.geometry('400x400')
tk.Button(app, text="Top Side 1").pack(side="top")
tk.Button(app, text="Top Side 1").pack(side="top")
tk.Button(app, text="right Side 1").pack(side="right")
tk.Button(app, text="right Side 2").pack(side="right")
tk.Button(app, text="bottom Side 1").pack(side="bottom")
tk.Button(app, text="bottom Side 2").pack(side="bottom")
tk.Button(app, text="left side 1").pack(side="left")
tk.Button(app, text="left Side 2").pack(side="left")
app.mainloop()
