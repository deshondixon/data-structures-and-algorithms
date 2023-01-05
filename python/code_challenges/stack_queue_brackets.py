from data_structures.stack import Stack


def multi_bracket_validation(string):
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}
    for x in string:
        if x in brackets:
            stack.push(x)
        elif x in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != x:
                return False
    return stack.is_empty()
