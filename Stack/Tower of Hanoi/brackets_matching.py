def is_balanced(string):
    stack = []
    for ch in string:
        if ch in ['(', '{', '[']:
            stack.append(ch)
        else:
            if ch == ')' and stack and stack[-1] == '(':
                stack.pop()
            if ch == '}' and stack and stack[-1] == '{':
                stack.pop()
            if ch == ']'and stack and stack[-1] == '[':
                stack.pop()
    return False if stack else True


sample = '{}{}((()(())[]))()'

print(is_balanced(sample))
