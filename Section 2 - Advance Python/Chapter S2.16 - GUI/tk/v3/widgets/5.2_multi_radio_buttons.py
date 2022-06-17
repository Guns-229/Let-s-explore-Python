import tkinter as tk

def display_choice():
    print(choice.get())
    print(rating.get())

root = tk.Tk()

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress select the OS on which to Install",
         fg="light blue",
         bg="Dark blue").pack()

choice = tk.StringVar()
rating = tk.StringVar()

lst = ["Windows", "Linux", "OpenBSD", "Solaris", "macOS", "ReactOS"]

for os_val in lst:
    tk.Radiobutton(root, text=os_val, variable=choice,
                   value=os_val).pack()


for os_rating in range(11):
    tk.Radiobutton(root, text=os_rating,
                   variable=rating, value=os_rating).pack()

tk.Button(root, text="Next", command=display_choice).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
