#!/usr/bin/env python3

"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

import unittest
from queue import LifoQueue


def is_balanced(s):
    association = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    opening_bracket_stack = LifoQueue()

    if len(s) == 0:
        return False

    for c in s:
        if c in association:
            opening_bracket_stack.put(c)
        else:
            if opening_bracket_stack.qsize() == 0:
                return False
            last_inserted_opening_bracket = opening_bracket_stack.get()
            if association[last_inserted_opening_bracket] != c:
                return False

    if opening_bracket_stack.qsize() > 0:
        return False

    return True


class Test(unittest.TestCase):
    def test_is_balanced(self):
        self.assertEqual(True, is_balanced("([])[]({})"))

    def test_is_not_balanced(self):
        self.assertEqual(False, is_balanced("([)]"))
        self.assertEqual(False, is_balanced("{"))
        self.assertEqual(False, is_balanced(")"))
        self.assertEqual(False, is_balanced(""))


if __name__ == "__main__":
    unittest.main()
