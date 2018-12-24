//  This problem was asked by Google.

// An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

// If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

#include <stdio.h>
#include <inttypes.h>

struct Node
{
  int index;
  struct Node *both;
};

struct LinkedList
{
  struct Node *head;
};

struct Node *XOR(struct Node *a, struct Node *b)
{
  return (struct Node *)((uintptr_t)(a) ^ (uintptr_t)(b));
}

int add(struct LinkedList *list, struct Node *node)
{
  node->both = XOR(list->head, NULL);
  node->index = list->head->index + 1;
  list->head->both = XOR(node, list->head->both);
  list->head = node;
  return node->index;
}

struct Node *get(struct LinkedList *list, int index)
{
  struct Node *current = list->head;
  struct Node *previous = NULL;
  struct Node *next;

  while (current != NULL)
  {
    if (index == current->index)
    {
      return current;
    }
    next = XOR(previous, current->both);
    previous = current;
    current = next;
  }
}

int main()
{
  // define the first node
  struct Node head = {0, NULL};

  // initialize the list with the first node
  struct LinkedList list = {&head};

  // add some nodes to the list
  struct Node node1;
  struct Node node2;
  add(&list, &node1);
  add(&list, &node2);

  for (int i = 0; i <= list.head->index; i++)
  {
    printf("node %d address: %p\n", i, get(&list, i));
    printf("node %d both:    %p\n", i, get(&list, i)->both);
  }

  printf("\n");

  // head cursor is used to add the nodes to the list, the code can easily be altered to add each node at the "end" instead but it's basically the same thing
  printf("head is now at the last index: %d\n", (*list.head).index);
  printf("head both:    %p\n", (*list.head).both);
  printf("head address: %p\n", list.head);

  return (0);
}