#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""  This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

class Node:
  def __init__(self, value, left = None, right = None):
    self.left = left
    self.right = right
    self.value = value

c1 = Node("1")
c2 = Node("1")
b1 = Node("1", c1, c2)
b2 = Node("0")
a1 = Node("1")
a2 = Node("0", b1, b2)
root = Node("root", a1, a2)

def is_unival_subtree(tree):
  if (tree.left and tree.left.value != tree.value):
    return False
  if (tree.right and tree.right.value != tree.value):
    return False
  return True

def count(node):
  amount = 0
  amount += count(node.left) if node.left else 0
  amount += count(node.right) if node.right else 0
  if (is_unival_subtree(node)):
    return amount + 1
  return amount

print count(root)