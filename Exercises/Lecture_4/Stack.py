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