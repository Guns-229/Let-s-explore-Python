#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

d = subprocess.run(["ls", "-l"])
print(d)
