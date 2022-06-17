import threading
import random
import time

def worker(num):
    """thread worker function"""
    x = random.randint(1,10)
    print ('Worker:', num, "Sleeping for", x)
    time.sleep(x)
    print ('Completed: Worker:', num)
    return

threads = []
for i in range(50):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
