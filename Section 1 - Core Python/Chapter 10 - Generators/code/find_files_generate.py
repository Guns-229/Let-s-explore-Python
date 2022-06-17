import os

# Finds files recursively
def find(path='.'):
    try:
        for item in os.listdir(path):
            fn = os.path.normpath(os.path.join(path, item))

            if os.path.isdir(fn):
                for f in find(fn):
                    yield f
            else:
                yield fn
    except Exception as e:
        pass

# At each interaction, the generator yeld a new file name
for fn in find(r"C:\apps"):
    print (fn)