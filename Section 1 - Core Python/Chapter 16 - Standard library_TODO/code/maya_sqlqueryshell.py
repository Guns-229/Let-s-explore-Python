"""Maya SQl Query Shell

Allows you to query sqlite db from command shell.
License: >= GNU 3.0
Author: Mayank Johri mayankjohri (a) gmail . com
url: TBD
Last date of update: 02 July 2018
"""
from cmd import Cmd
import sqlite3 as sqlite


class MyCMD(Cmd):
    def do_use(self, args):
        if len(args) == 2:
            self.conn = sqlite.connect(args[1])

    def do_select(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'John Doe'
        else:
            name = args
        print("Hello, %s" % name)

    def do_quit(self, args):
        """Quits the program."""
        print("Tschüss")
        raise SystemExit


if __name__ == '__main__':
    print("lets start")
    prompt = MyCMD()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
