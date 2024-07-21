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
    dq.deque = [*string]
    while dq.size() > 1:
        if not (dq.removeFront() == dq.removeTail()):
            return False
    return True  


