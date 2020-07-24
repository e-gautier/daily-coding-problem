#!/usr/bin/env python3

"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


def remove_kth_from_end(node, k):
    previous = node
    kth = node
    end = node

    for _ in range(0, k):
        end = end.next

    while end != None:
        previous = kth
        end = end.next
        kth = kth.next

    previous.next = kth.next


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def display(self):
        node = self
        while node != None:
            print(node.value, end="-")
            node = node.next
        print()


node5 = Node(6)
node4 = Node(5, node5)
node3 = Node(4, node4)
node2 = Node(2, node3)
head = Node(1, node2)

head.display()
remove_kth_from_end(head, 4)
head.display()

head = Node(5)

head.display()
remove_kth_from_end(head, 1)
head.display()

node5 = Node(9)
node4 = Node(9, node5)
node3 = Node(5, node4)
node2 = Node(2, node3)
head = Node(1, node2)

head.display()
remove_kth_from_end(head, 1)
head.display()
