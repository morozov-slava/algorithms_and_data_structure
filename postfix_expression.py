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


def calculate_postfix_expression(exp: str):
    s1 = Stack()
    s2 = Stack()
    s1.stack = [x for x in exp]
    while s1.size() > 0:
        pop_value = s1.pop()
        if pop_value.isdigit():
            s2.push(int(pop_value))
        elif pop_value == "+":
            v1 = s2.pop()
            v2 = s2.pop()
            s2.push(v1 + v2)
        elif pop_value == "*":
            v1 = s2.pop()
            v2 = s2.pop()
            s2.push(v1 * v2)
        elif pop_value == "=":
            break 
        else:
            raise AssertionError("Postfix expression contains unknown values")
    return s2.peek()




