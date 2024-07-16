class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size():
            return self.stack.pop(0)
        else:
            return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size():
            return self.stack[0]
        else:
            return None


class TestStack:

    @staticmethod
    def test_size():
        stack_obj = Stack()
        assert stack_obj.size() == 0
        stack_obj.push(10)
        assert stack_obj.size() == 1
        stack_obj.pop()
        assert stack_obj.size() == 0

    @staticmethod
    def test_pop():
        stack_obj = Stack()
        stack_obj.push(10)
        stack_obj.push(3)
        stack_obj.push(4)
        assert stack_obj.pop() == 4
        assert stack_obj.pop() == 3
        assert stack_obj.pop() == 10

    @staticmethod
    def test_push():
        stack_obj = Stack()
        stack_obj.push(10)
        assert stack_obj.stack == [10]
        stack_obj.push(7)
        assert stack_obj.stack == [7, 10]

    @staticmethod
    def test_peek():
        stack_obj = Stack()
        stack_obj.push(10)
        assert stack_obj.peek() == 10
        stack_obj.push(7)
        assert stack_obj.peek() == 7


def test_stack():
    TestStack.test_size()
    TestStack.test_pop()
    TestStack.test_push()
    TestStack.test_peek()
    return True



