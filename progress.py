#!/usr/bin/env python
# coding=utf-8
from time import sleep
import sys


for _ in range(100):
    for x in ["/", "-", "\\", "|", "-"]:
        print(x, end="", flush=True)
        sleep(0.01)
        print("\b", end="")


