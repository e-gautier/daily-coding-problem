#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# This problem was asked by Uber.

#  Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

arr = [1, 2, 3, 4, 5]

# result 1 (better but lookout in case of presence of 0 in the list)
result = list(arr)
product = 1
for i in range(len(arr)):
  product*=arr[i]
for i in range(len(arr)):
  result[i] = product/arr[i]

# result 2 (without division)
result = [1] * len(arr)
for i, e in enumerate(arr):
  for e2 in arr:
    if (e == e2):
      continue
    result[i] *= e2

print(result)