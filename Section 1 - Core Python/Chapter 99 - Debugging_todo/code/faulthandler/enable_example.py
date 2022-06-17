import faulthandler as fh
import ctypes


fp = open("error_auto.log", "a+")
fh.enable(file=fp, all_threads=True)

ctypes.string_at(10)

