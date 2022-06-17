import tkinter as tk

def display_choice():
    print(choice.get())

root = tk.Tk()

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed",
         fg="light blue",
         bg="Dark blue").pack()

choice = tk.IntVar()


tk.Radiobutton(root, text="OpenSSL", variable=choice,
               value=10).pack()
tk.Radiobutton(root, text="SSL", variable=choice,
               value=20).pack()
tk.Radiobutton(root, text="XYZ SSL", variable=choice,
               value=30).pack()
tk.Button(root, text="Next", width=20, command=display_choice).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
