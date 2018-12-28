#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

encoded_string = "111"

def decode(s):
  if (len(s) == 1):
    return isValid(s)
  if (len(s) == 2):
    return isValid(s) + 1
  return isValid(s[:1]) * decode(s[1:]) + isValid(s[:2]) * decode(s[2:])

def isValid(s):
  if (int(s) > 0 and int(s) < 27):
    return 1
  return 0

print decode(encoded_string)