class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() > 0:
            return self.stack[0]
        return None


class StackQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self): 
        if self.s2.size():
            return self.s2.pop()
        if self.s1.size() == 0:
            return None
        while self.s1.size() > 1:
            self.s2.push(self.s1.pop())
        return self.s1.pop()

    def size(self):
        return self.s1.size() + self.s2.size()



