#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# This problem was asked by Stripe.

#  Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

arr = [3, 4, -1, 1]
arr = [1, 2, 0]
higher = None
lower = None

for e in arr:
  sup = e+1
  inf = e-1
  if (sup not in arr and higher is None):
    higher = sup
  if (inf >= 0 and inf not in arr and lower is None):
    lower = inf

if (lower is not None):
  print(lower)
else:
  print(higher)