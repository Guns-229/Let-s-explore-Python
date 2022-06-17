import tkinter as tk

def display_choice():
    print(choice.get())

root = tk.Tk()

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed",
         fg="light blue",
         bg="Dark blue").pack()

choice = tk.IntVar()


tk.Checkbutton(root, text="OpenSSL", variable=choice).pack()
tk.Checkbutton(root, text="SSL", variable=choice).pack()
tk.Checkbutton(root, text="XYZ SSL", variable=choice).pack()

tk.Button(root, text="Next", width=20, command=display_choice).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
