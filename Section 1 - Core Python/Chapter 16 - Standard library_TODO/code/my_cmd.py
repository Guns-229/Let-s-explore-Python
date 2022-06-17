from cmd import Cmd

class MyCMD(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'John Doe'
        else:
            name = args
        print ("Hello, %s" % name)

    def do_quit(self, args):
        """Quits the program."""
        print("Tschüss")
        raise SystemExit


if __name__ == '__main__':
    print("lets start")
    prompt = MyCMD()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
