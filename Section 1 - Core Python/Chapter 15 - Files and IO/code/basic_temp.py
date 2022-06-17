import tempfile
from time import sleep

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
print(fp.read())
sleep(10)
fp.close()



