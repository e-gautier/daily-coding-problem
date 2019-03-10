#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
import unittest

def parse(k, s):
  """
  k distinct char
  s the string to test
  """

  tmpStr = ""
  longestStr = ""
  amountOfDistinctChar = 0
  if k == 0:
    return longestStr
  for i, c in enumerate(s):
    for char in s[i::]: # O(n²)
      if char not in tmpStr:
        if amountOfDistinctChar >= k:
          longestStr = tmpStr if len(tmpStr) > len(longestStr) else longestStr
          tmpStr = ""
          amountOfDistinctChar = 0
          break
        amountOfDistinctChar += 1
      tmpStr += char
  return longestStr if len(longestStr) > 0 else s

class Test(unittest.TestCase):
  def testSVariable(self):
    self.assertEqual("bcb", parse(2, "bcb"))
    self.assertEqual("bcb", parse(2, "abcba"))
    self.assertEqual("ab", parse(2, "abca"))
    self.assertEqual("bddd", parse(2, "abcbddda"))
  def testKVariable(self):
    self.assertEqual("abcba", parse(3, "abcbad"))
    self.assertEqual("abcbad", parse(4, "abcbad"))
    self.assertEqual("", parse(0, "abcbad"))

if __name__ == "__main__":
  unittest.main()