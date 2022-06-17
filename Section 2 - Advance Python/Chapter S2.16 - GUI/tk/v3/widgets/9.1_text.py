import tkinter as tk

root = tk.Tk()
txtbox = tk.Text(root, height=10, width=90)
txtbox.pack(expand=tk.YES, side=tk.LEFT)

txtbox.insert(tk.END, """Python provides many libraries which cater Linux & BSD specific needs. In this
              section we are going to cover few of them. Most common modules which we are going to
              cover are as follows""")

tk.Button(root, text="Quit", command=root.destroy ).pack()

root.mainloop()
