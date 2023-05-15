from typing import Optional

class Node:
    def __init__(self, key: int):
        self.key = key
        self.next : Optional[Node] = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        val = self.head.key
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val
    

n = int(input())
queue = Queue()
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'E':
        queue.enqueue(int(cmd[1]))
    elif cmd[0] == 'D':
        val = queue.dequeue()
        if val is not None:
            print(val)