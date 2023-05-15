from typing import Optional

class Node:
    def __init__(self, key: int):
        self.key = key
        self.next : Optional[Node] = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        val = self.top.key
        self.top = self.top.next
        return val
    
    def isEmpty(self):
        return self.top is None

n = int(input())
stack = Stack()
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'PU':
        stack.push(int(cmd[1]))
    elif cmd[0] == 'PO':
        val = stack.pop()
        if val is not None:
            print(val)