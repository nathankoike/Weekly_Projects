"""
Auth: Nate Koike
Date: 1 November 2019
Desc: test code for the stack
"""

import stack

def main():
    # # test a list-based stack
    # St = stack.Stack()
    # St.push(1)
    # print(St.top())
    # St.push(7)
    # St.pop()
    # print(St.top())
    # St.pop()
    # print(St.empty())

    # # test a node-based stack
    # St = stack.Stack()
    # St.push(1)
    # print(St.top())
    # St.push(7)
    # St.pop()
    # print(St.top())
    # St.pop()
    # print(St.empty())

    # test a singly linked list
    ls = stack.SinglyLinkedList()
    print(ls.size()) # should be 0
    ls.add(1)
    ls.add(3)
    ls.add(5)
    print(ls.get_at(0)) # should be 1
    print(ls.get_at(2)) # should be 5
    ls.remove_at(0)
    print(ls.get_at(0)) # should be 3
    ls.remove()
    print(ls.size()) # should be 1
    print(ls.get_at(0)) # should be 3

if __name__ == "__main__":
    main()
