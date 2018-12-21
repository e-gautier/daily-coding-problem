#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#  This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

k = 17
arr = [10, 15, 3, 7]
tmp = [False] * k
for e in arr:
  if (tmp[k-e]):
    print(k-e, e)
  tmp[e] = True