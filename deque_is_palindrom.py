class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)
        
    def removeFront(self):
        if len(self.deque):
            return self.deque.pop(0)

    def removeTail(self):
        if len(self.deque):
            return self.deque.pop()

    def size(self):
        return len(self.deque)


def is_palindrome(string: str):
    dq = Deque()
    for i in range(len(string) // 2):
        dq.addFront(string[i])
        dq.addTail(string[-(i+1)])
        if not (dq.removeFront() == dq.removeTail()):
            return False
    return True




