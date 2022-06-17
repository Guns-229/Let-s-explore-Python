import time
import sys

def fib():
   a, b = 0, 1
   while a < 10:
      yield b
      a, b = b, a + b


iter = list(fib())
print(iter)

iter = fib()
print("LETS START AFTER THIS")
try:
   for i in iter:
      print( i),
      time.sleep(1)
      sys.stdout.flush()
except KeyboardInterrupt:
   print( "Calculation stopped")
