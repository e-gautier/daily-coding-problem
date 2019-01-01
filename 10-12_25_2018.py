#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time
import threading

def f():
  print("f")

n = 1000

def scheduler(n, f):
  time.sleep(n/1000)
  return f()

t = threading.Thread(target=scheduler, args=(n, f))
t.start()

print("end")
t.join()