import os

# Finds files recursively
def find_files(path='.'):
    try:
        lst = []
        for item in os.listdir(path):
            fn = os.path.normpath(os.path.join(path, item))

            if os.path.isdir(fn):
                for f in find_files(fn):
                    lst.append(f)
            else:
                lst.append(fn)
        return lst
    except Exception as e:
        print("Error:", e)
        return lst
        

# At each interaction, the generator yeld a new file name
for fn in find_files("C:\\apps"):
    print (fn)