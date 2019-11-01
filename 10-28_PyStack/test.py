"""
Auth: Nate Koike
Date: 1 November 2019
Desc: test code for the stack
"""

import stack

def main():
    St = stack.Stack()

    St.push(1)

    print(St.top())

    St.push(7)

    St.pop()

    print(St.top())

    St.pop()

    print(St.empty())

if __name__ == "__main__":
    main()
