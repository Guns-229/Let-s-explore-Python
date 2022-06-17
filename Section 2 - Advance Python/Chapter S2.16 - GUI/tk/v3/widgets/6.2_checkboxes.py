import tkinter as tk

def display_choice():
    print(openssl.get(), ssl.get(), xyzssl.get())

root = tk.Tk()

tk.Label(text = "Welcome to SoftGrid Helper Installation\n\tPress next to proceed", 
         fg="light blue",
         bg="Dark blue").pack()


openssl = tk.IntVar()
ssl = tk.IntVar()
xyzssl = tk.IntVar()
lst = [openssl, ssl, xyzssl]

for l in lst:
    var = [k for k,v in locals().items() if v == l][0]
    tk.Checkbutton(root, text=var, variable=l).pack()
tk.Button(root, text="Next", width=20, command=display_choice).pack()
tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
