import faulthandler
faulthandler.enable()

try:
    a = 1/0
except Exception as e:
    with open("error.log", "a+") as f:
        faulthandler.dump_traceback(file=f, all_threads=True)

