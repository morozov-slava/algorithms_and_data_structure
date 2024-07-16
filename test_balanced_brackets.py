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
    i = 0
    i_r = 0
    i_l = 0
    while i < len(brackets):
        if (brackets[i] == ")") and (stack_obj.peek() is None):
            return False
        elif (brackets[i] == "(") and (not stack_obj.peek() == "("):
            stack_obj.push(brackets[i])
            i_l = i
            i += 1
        elif (brackets[i] == ")") and (stack_obj.peek() == "(") and (i > i_r):
            stack_obj.push(brackets[i])
            i_r = i
            i = i_l + 1
        else:
            i += 1
    return stack_obj.size() == len(brackets)



def test_brackets_are_balanced():
    assert brackets_are_balanced("(())") is True
    assert brackets_are_balanced("()") is True
    assert brackets_are_balanced("()()()") is True
    assert brackets_are_balanced("()(())()") is True
    assert brackets_are_balanced("())()()") is False
    assert brackets_are_balanced("())()()") is False
    assert brackets_are_balanced("(()()())") is True
    assert brackets_are_balanced(")((()))") is False
    assert brackets_are_balanced("())))(((()") is False
    assert brackets_are_balanced("()((()))") is True
    return True




