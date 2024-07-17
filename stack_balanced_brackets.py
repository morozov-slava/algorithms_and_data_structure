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


def brackets_are_balanced(brackets: str):
    if len(brackets) == 0:
        raise AssertionError("Given string is empty")
    stack_obj = Stack()
    for i in range(len(brackets)):
        if brackets[i] == "(":
            stack_obj.push(brackets[i])
        elif brackets[i] == ")":
            if not stack_obj.size():
                return False
            stack_obj.pop()
    return stack_obj.size() == 0








