import os
 
def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_name in files:
            print( os.path.join(root, file_name) )
 
if __name__ == '__main__':
    pywalker('/var')
