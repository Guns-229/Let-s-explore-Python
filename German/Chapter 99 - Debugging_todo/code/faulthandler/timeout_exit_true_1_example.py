import faulthandler


def MySample():
    import time
    time.sleep(6)
    return "Welcome to the Wonders of Python"


faulthandler.dump_traceback_later(2, repeat=True, exit=True)
txt = MySample()
print(txt)
faulthandler.cancel_dump_traceback_later()
