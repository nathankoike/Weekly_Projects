"""
Auth: Nate Koike
Date: 1 November, 2019
Desc: create a module to implement a stack in python using both lists and nodes
"""

# a node for a singly linked list
class Node:
    # allow a node to be made without any data
    def __init__(self, val=None, next=None):
        self._value = val # the data in the node
        self._next = next # the next node

    # set the value of this node
    def set_val(self, value):
        self._value = value

    # get the value from this node
    def get_val(self):
        return self._value

    # set the node immediately following this node
    def set_next(self, next):
        self._next = next

    # get the node immediately following this node
    def get_next(self):
        return self._next

# a list but each node only points in one direction
class SinglyLinkedList:
    def __init__(self):
        # the pointer to the beginning of the list
        self._begin = None

        # the pointer to the end of the list
        self._end = None

        # the current number of nodes in the list
        self._size = 0

    # add an item to the end of the list
    def add(self, value):
        new_node = Node(val=item)

        # if the list is empty
        if not self._begin:
            self._begin = new_node

        # set the node after the last node to be the new node
        self._end.set_next(new_node)

        # update the end pointer to reflect this change
        self._end = new_node

        # lastly increase the size of the list
        self._size += 1

    # remove the last node in the list
    def remove(self):
        follow = self._begin

        # traverse the whole list
        for _ in range(self.size() - 2):
            follow = follow.get_next()

        # disconnect the last node
        follow.set_next(None)

        # update the end pointer to reflect this change
        self._end = follow

        # lastly, decrement the size of the list
        self._size -= 1

    # add a node at the given index
    def add_at(self, value, index):
        new_node = Node(val=value)
        follow = self._begin

        # traverse the list, stopping at the node before the desired index
        for _ in range(index - 2):
            follow = follow.get_next()

        # set the new node to point to the node currently at the desired index
        new_node.set_next(follow.get_next())

        # set the node before the desired index to point to the new node
        follow.set_next(new_node)

        # lastly, increment the size of the list to reflect this change
        self._size += 1

    # remove the node at the given index
    def remove_at(self, index):
        follow = self._begin

        # traverse the list, stopping at the node before the desired index
        for _ in range(index - 2):
            follow = follow.get_next()

        # set the current node to skip over the node to be deleted. python's
        # garbage collection will handle the rest for us
        follow.set_next(follow.get_next())

        # lastly, decrement the size of the list to reflect this change
        self._size -= 1

    # return the value at the desired index
    def get_at(self, index):
        follow = self._begin

        # don't allow indexing outside of the bounds of the list
        index = index % self.size()

        for _ in range(index - 1):
            follow = follow.get_next()

        return follow.get_val()

class Stack:
    # allow the stack to be initialized with or without a top value
    def __init__(self, top=None):
        self._top = top

    def push(self, value):
        # create a new node containing the desired value immidiately before the
        # top of this stack
        new_node = Node(val=value, next=self._top)

        # set the top of the stack to reflect this new addition
        self._top = new_node

    def top(self):
        if self.empty():
            return None

        return self._top.get_val()

    def pop(self):
        if self.empty():
            return

        # set the top to point to the node immediately following this one
        # we don't need to do more than this because python's garbage collection
        # will clean up the pointers for us
        self._top = self._top.get_next()

    def empty(self):
        # check to see if the top pointer is null
        return self._top == None

# a list-based stack implementation
class L_Stack:
    # the constructor for an empty stack
    def __init__(self):
        self._stack = []

    # add something to the end of the stack
    def push(self, item):
        self._stack.append(item)

    # look at the most recent item in the stack
    def top(self):
        # if the stack is empty return nothing
        if self.empty():
            return None

        # return the most recently added item
        return self._stack[-1]

    # remove an item from the stack
    def pop(self):
        # if the stack is empty we cannot pop anything
        if self.empty():
            return

        # set the stack equal to the slice of itself from the beginning to one
        # value from the top
        self._stack = self._stack[0:len(self._stack) - 1]

    # check to see if the stack is empty
    def empty(self):
        return len(self._stack) == 0
