import tkinter as tk

root = tk.Tk()

tk.Button(root, text="Hello 1").pack(fill=tk.X)
tk.Button(root, text="Hello 2").pack(fill=tk.X)
tk.Button(root, text="Hello L 1" ).pack(side=tk.LEFT,
                                        fill=tk.X)
tk.Button(root, text="Hello R 1").pack(side=tk.RIGHT,
                                       fill=tk.X)
tk.Button(root, text="Hello Special").pack(side=tk.LEFT, padx=5, pady=10,
                                           expand=tk.YES, fill=tk.X)
tk.Button(root, text="Hello R 2").pack(side=tk.RIGHT, fill=tk.X)

tk.mainloop()
