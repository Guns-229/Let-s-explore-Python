import tempfile
from time import sleep
import os

try:
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        # sleep(20)
        file_name = os.path.join(tmpdirname, "myfile.txt")
        print(file_name)
        with open(file_name, "w") as fp:
            fp.write("Hello world")
        # sleep(20)
        # a = 1/0
        print("This should never ever get executed.")
        sleep(20)
        print("timeout ")
except Exception as e:
    print("Error:", e)
