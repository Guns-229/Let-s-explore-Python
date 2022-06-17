
with open('myfile.txt', "w") as myFile:
    for a in ["a", "b", "c"]:
        myFile.write(str(a))
    for a in [1,2,3,4,5,"6"]:
        myFile.write(str(a))

try:
    myFile.write("ERRRRR")
except:
    print("Error, what are you trying to do with closed file")
