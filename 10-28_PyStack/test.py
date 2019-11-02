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
    ls.print_list() # should be [1, 3, 5]
    ls.add_at(0, 0) # should add 0 at index 0
    print(ls.get_at(0)) # should be 0
    ls.print_list() # should be [0, 1, 3, 5]
    ls.remove_at(0)
    ls.print_list() # should be [1, 3, 5]
    ls.remove()
    ls.print_list() # should be [1, 3]
    ls.add_at(2, 1)
    ls.print_list() # should be [1, 2, 3]

if __name__ == "__main__":
    main()
