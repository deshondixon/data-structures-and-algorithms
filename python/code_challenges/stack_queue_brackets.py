from data_structures.stack import Stack


def multi_bracket_validation(string):
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}
    for char in string:
        if char in brackets:
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False
    return stack.is_empty()
