#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

arr = [5, 1, 1, 5]
arr = [2, 4, 6, 2, 5]

mid_list = int((len(arr)-1)/2)

def get_sum(arr):
  s1 = 0
  s2 = 0
  s3 = 0
  for i in range(0, mid_list, 2):
    # add first one and last one, 2 by 2, until the middle of the list
    s1 += arr[i] + arr[-(i+1)]
  # exception: if the highest index is even (amount of elements is odd then), add the middle one
  if (mid_list % 2 == 0):
    s1 += arr[mid_list]
  for i in range(0, len(arr)-1, 2):
    s2 += arr[i]
  for i in range(1, len(arr)-1, 2):
    s3 += arr[i]
  return (s1, s2, s3)

def get_higher_sum(sum):
  return max(sum)

print(get_higher_sum(get_sum(arr)))