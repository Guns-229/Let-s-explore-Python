import tkinter as tk

def display_choice():
    print(choice.get())

root = tk.Tk()

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress select the OS on which to Install",
         fg="light blue",
         bg="Dark blue").pack()

choice = tk.StringVar()

lst = ["Windows", "Linux", "OpenBSD", "Solaris", "macOS", "ReactOS"]

for os_val in lst:
    tk.Radiobutton(root, text=os_val, variable=choice,
                   value=os_val).pack()


tk.Button(root, text="Next", command=display_choice).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
