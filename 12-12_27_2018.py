#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2 

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
import unittest

steps = 4
X = [1, 2]

def ways(steps):
  if (steps == 1):
    return 1
  if (steps == 2):
    return 2
  return ways(steps-1) + ways(steps-2)

def restrictedWays(steps, X):
  ways = 0
  for x in X:
    if (steps == x):
      ways += 1
    if (steps > x):
      ways += restrictedWays(steps-x, X)
  return ways

class Test(unittest.TestCase):
  def testWays(self):
    self.assertEqual(5, ways(steps))
  def testRestrictedWays(self):
    self.assertEqual(5, restrictedWays(steps, X))

if __name__ == '__main__':
    unittest.main()