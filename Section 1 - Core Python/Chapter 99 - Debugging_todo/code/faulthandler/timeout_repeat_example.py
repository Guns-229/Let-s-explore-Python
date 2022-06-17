import faulthandler


def MySample():
    import time
    time.sleep(3)
    return "Welcome to the Wonders of Python"


log_file = "dump_later.txt"
f = open(log_file, "w")
faulthandler.dump_traceback_later(2, file=f, repeat=True)
txt = MySample()
print(txt)
f.close()
faulthandler.cancel_dump_traceback_later()

with open(log_file) as fp:
    for line in fp.readlines():
        print(line, end="")
