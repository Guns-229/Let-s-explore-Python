import faulthandler


def MySample():
    import time
    time.sleep(10)
    return "Welcome to the Wonders of Python"


faulthandler.dump_traceback_later(5)
MySample()
