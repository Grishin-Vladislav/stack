class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self) -> bool:
        if self.stack:
            return False
        return True

    def push(self, elem) -> None:
        self.stack.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)


def is_valid_parenthesis(string: str) -> bool:
    stack = Stack()
    full_brackets = ('()', '[]', '{}')
    for element in string:
        if element in (')', ']', '}'):
            if stack.is_empty():
                return False
            elif stack.peek() + element in full_brackets:
                stack.pop()
            else:
                return False

        elif element in ('(', '[', '{'):
            stack.push(element)

    if not stack.is_empty():
        return False
    return True


assert not is_valid_parenthesis('[[{{}}]')
assert not is_valid_parenthesis('[(])')
assert not is_valid_parenthesis('((')
assert is_valid_parenthesis('()')
assert is_valid_parenthesis('()()()()[]')
