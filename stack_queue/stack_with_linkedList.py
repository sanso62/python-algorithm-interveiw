class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
    def push(self, item):
        self.last = Node(item, self.last)
    def pop(self):
        result = self.last.item
        self.last = self.last.next
        return result

if __name__=="__main__":
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    for _ in range(3):
        print(stack.pop())
