#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#  This problem was asked by Google.

#  Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

import re

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def toString(self):
    if (self.left is None):
      left = ''
    else:
      left = self.left.toString()
    if (self.right is None):
      right = ''
    else:
      right = self.right.toString()
    return '{name:'+ self.val + ',left:' + left + ',right:' + right + '}'

  def toObj(self, s):
    namePattern = re.search('name:([a-zA-Z.]+),', s)
    leftPattern = re.search('left:({.+}),', s)
    rightPattern = re.search('right:({.+})', s)
    if (leftPattern is None):
      left = None
    else:
      left = leftPattern.group(1)
      left = Node('').toObj(left)
    if (rightPattern is None):
      right = None
    else:
      right = rightPattern.group(1)
      right = Node('').toObj(right)
    return Node(namePattern.group(1), left, right)


def serialize(root):
  return root.toString()

def deserialize(s):
  return Node('').toObj(s)

# test
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left', 'nope'
print(serialize(node))
print(deserialize(serialize(node)).left.left.val)
print(serialize(deserialize(serialize(node))))