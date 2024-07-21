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


class TestDeque:
    
    @staticmethod
    def test_addFront():
        dq = Deque()
        assert len(dq.deque) == 0
        dq.addFront(2)
        assert len(dq.deque) == 1
        dq.addFront(3)
        assert dq.deque[0] == 3
        assert dq.deque[1] == 2
        dq.addFront(10)
        assert dq.deque[0] == 10
        assert dq.deque[1] == 3
        assert dq.deque[2] == 2

    @staticmethod
    def test_addTail():
        dq = Deque()
        assert len(dq.deque) == 0
        dq.addTail(2)
        assert len(dq.deque) == 1
        dq.addTail(3)
        assert dq.deque[0] == 2
        assert dq.deque[1] == 3
        dq.addTail(10)
        assert dq.deque[0] == 2
        assert dq.deque[1] == 3
        assert dq.deque[2] == 10

    @staticmethod
    def test_removeFront():
        dq = Deque()
        dq.addFront(2)
        assert (2 in dq.deque)
        dq.addFront(3)
        assert (3 in dq.deque)
        dq.addFront(10)
        assert (10 in dq.deque)
        assert len(dq.deque) == 3
        dq.removeFront()
        assert (10 not in dq.deque)
        assert len(dq.deque) == 2
        assert dq.deque[0] == 3
        assert dq.deque[1] == 2
        dq.removeFront()
        assert (3 not in dq.deque)
        assert len(dq.deque) == 1
        assert dq.deque[0] == 2
        dq.removeFront()
        assert len(dq.deque) == 0

    @staticmethod
    def test_removeTail():
        dq = Deque()
        dq.addTail(2)
        assert (2 in dq.deque)
        dq.addTail(3)
        assert (3 in dq.deque)
        dq.addTail(10)
        assert (10 in dq.deque)
        dq.removeTail()
        assert (10 not in dq.deque)
        assert len(dq.deque) == 2
        dq.removeTail()
        assert (3 not in dq.deque)
        assert len(dq.deque) == 1
        assert dq.deque[0] == 2
        dq.removeTail()
        assert len(dq.deque) == 0

def test_deque():
    TestDeque.test_addFront()
    TestDeque.test_addTail()
    TestDeque.test_removeFront()
    TestDeque.test_removeTail()
    return True




