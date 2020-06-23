class Stack:
    def __init__(self, name):
        self.data = []
        self.name = name

    def empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.empty():
            return RuntimeError('The stack is empty. Cannot pop.')
        else:
            return self.data.pop()

    def peek(self):
        if self.empty():
            return RuntimeError('The stack is empty. Cannot peek.')
        else:
            return self.data[-1]

    def size(self):
        return len(self.data)
