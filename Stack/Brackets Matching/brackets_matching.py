import sys

sys.path.append("stack")
from stack import Stack


def is_balanced(string):
    stack = Stack("Brackets")
    for ch in string:
        if ch in ["(", "{", "["]:
            stack.push(ch)
        else:
            if ch == ")" and not stack.empty() and stack.peek() == "(":
                stack.pop()
            if ch == "}" and not stack.empty() and stack.peek() == "{":
                stack.pop()
            if ch == "]" and not stack.empty() and stack.peek() == "[":
                stack.pop()
    return False if stack else True


sample = "{}{}((()(())[]))()"

print(is_balanced(sample))
