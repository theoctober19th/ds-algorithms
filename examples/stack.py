from data_structures.stack import Stack

# creating a new stack
stack = Stack()

print('Pushing some values into the stack.')
stack.push('A')
stack.push('B')
stack.push('C')

print('Peeking into the stack.')
print(stack.peek())

print('Popping the values from the stack.')
print(stack.pop())
print(stack.pop())
print(stack.pop())
