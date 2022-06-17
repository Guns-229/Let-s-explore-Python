import tkinter as tk

root = tk.Tk()

def show_text():
    txtbox.insert(tk.END, """Python provides many libraries which cater Linux & BSD specific needs. In this
                  section we are going to cover few of them. Most common modules which we are going to
                  cover are as follows""")


txtbox = tk.Text(root, height=10, width=100)
sb = tk.Scrollbar(root, command=txtbox.yview)
txtbox.config(yscrollcommand=sb.set)

sb.pack(side=tk.RIGHT, fill=tk.Y)
txtbox.pack(side=tk.LEFT, fill=tk.Y)
root.mainloop()
