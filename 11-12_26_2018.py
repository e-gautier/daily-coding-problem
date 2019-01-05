#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

s = "d"
words = ["dog", "deer", "deal"]

# first solution
for w in words:
  if (w[:len(s)] == s):
    print(w)

# second solution (search tree)
class Node:
  def __init__(self, char):
    self.value = char
    self.lefs = {}
  def load(self, char):
    if (char in self.lefs):
      return self.lefs[char]
    n = Node(char)
    self.lefs[char] = n
    return n
  def find(self, c):
    if (c in self.lefs):
      return self.lefs[c]
    return None
  def toString(self):
    r = []
    for char, n in self.lefs.items():
      if (len(n.lefs) == 0):
        r.append(char)
      for s in n.toString():
        r.append(char+s)
    return r

class Tree:
  def __init__(self):
    self.head = Node('^')
  def load(self, word):
    n = self.head
    for char in word:
      n = n.load(char)
  def find(self, s):
    n = self.head
    for c in s:
      n = n.find(c)
      if (n is None):
        return None
    return n.toString()

def search(arr, s):
  tree = Tree()

  # build the tree
  for word in arr:
    tree.load(word)

  # find in tree
  r = tree.find(s)
  if (r is None):
    return None
  r = list(r)
  for i, char in enumerate(r):
    r[i] = s+char
  return r

print(search(words, s))