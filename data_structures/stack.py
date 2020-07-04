class Stack:
    """
    Implementation of stack using python list
    """

    def __init__(self, name='stack'):
        # this list will hold the items in our stack
        self.data = []
        # the name of the stack, if we want later print the name of a
        # particular stack
        self.name = name

    def empty(self):
        '''Returns whether the stack is empty'''
        return len(self.data) == 0

    def push(self, value):
        '''push the given value into the stack'''
        self.data.append(value)

    def pop(self):
        '''Removes the value from the top of the stack and returns it.'''
        if self.empty():
            return RuntimeError("The stack is empty. Cannot pop.")
        else:
            return self.data.pop()

    def peek(self):
        '''Returns the vlaue from the top of the stack without removing it'''
        if self.empty():
            return RuntimeError("The stack is empty. Cannot peek.")
        else:
            # index -1 means the last element of the list
            return self.data[-1]

    @property
    def size(self):
        '''Returns the number of elements in the stack'''
        return len(self.data)
