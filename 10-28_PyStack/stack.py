"""
Auth: Nate Koike
Date: 1 November, 2019
Desc: create a module to implement a stack in python using both lists and nodes
"""

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
