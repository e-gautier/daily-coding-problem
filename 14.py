#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import unittest
import random
import math

"""
Monte Carlo method says if r = 1:
(π/4) = pointsInsideTheCircle/totalRandomPoint
so
π = (pointsInsideTheCircle/totalRandomPoint)*4
"""

def pointInCircle(r, x, y):
  return 1 if x**2+y**2 <= r**2 else 0

def approximatePi(r, totalRandomPoint):
  pointsInsideTheCircle = 0
  for i in range(totalRandomPoint):
    x = random.random()*r
    y = random.random()*r
    pointsInsideTheCircle = pointsInsideTheCircle + pointInCircle(r, x, y)
  return (pointsInsideTheCircle / totalRandomPoint) * 4

class Test(unittest.TestCase):
  def testApproximatePi(self):
    self.assertEqual(3.141, float(str(approximatePi(1, 100000000))[:5]))
    self.assertEqual(3.141, float(str(approximatePi(2, 100000000))[:5]))
    self.assertEqual(3.141, float(str(approximatePi(3, 100000000))[:5]))

if __name__ == "__main__":
  unittest.main()
