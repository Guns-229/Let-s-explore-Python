import sys
import os

def find_file(file_name):
    sel = ";"

    if os.sep == "/":
        sel = ':'
    for folder in os.environ['PATH'].split(sel):
        abs_path = os.path.join(folder, file_name)
        if os.path.exists(abs_path):
            return True, abs_path
    return False, ""


if __name__ == '__main__':
    print(find_file("java"))
