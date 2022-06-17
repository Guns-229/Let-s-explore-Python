import tempfile
import os


# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    file_name = os.path.join(tmpdirname, "myfile.txt")
    print(file_name)
    with open(file_name, "w") as fp:
        fp.write("Hello world")
    from time import sleep
    sleep(20)
    print("timeout, delete the temp folder along with files")

print(f"{os.path.exists(file_name)}")
# directory and contents have been removed
