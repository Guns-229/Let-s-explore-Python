from contextlib import ExitStack
filenames = ("foo.txt", "my_text.txt")


with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    for f in files:
        print(f.read())
