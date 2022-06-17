from threading import Thread
import faulthandler
import signal
import time


def do():
    time.sleep(30)


def main():
    threads = []
    for _ in range(1, 10):
        t = Thread(target=do, args=())
        t.start()
    for x in threads:
        x.join()


if __name__ == '__main__':
    faulthandler.register(signal.SIGUSR2)
    main()

