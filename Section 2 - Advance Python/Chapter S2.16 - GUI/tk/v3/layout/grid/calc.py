#!/usr/bin/env python3
from tkinter import Tk, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Entry, Style

class Calc(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Maya Calculator")
        Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')
        for a in range(4):
          self.columnconfigure(a, pad=3)
          self.rowconfigure(a, pad=3)
        self.rowconfigure(a + 1, pad=3)
        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=E+W+S+N)

        buttons = {}
        col = 0
        row = 1
        for a in ['Cls', 'Back', '', 'Close', 
                  "7", "8", "9", "/",
                  "4", "5", "6", "*",
                  "1", "2", "3", "-",
                  "0", ".", "=", "+"
                  ]:
          buttons[a] = Button(self, text=a)
          buttons[a].grid(row=row, column=col)
          col += 1
          if col % 4 == 0:
            col = 0
            row +=1

        self.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    # this removes the maximize button
    root.resizable(0,0)
    app = Calc()
    root.mainloop()


if __name__ == '__main__':
    main()
