from data_structures.linked_list import LinkedList, Node


class ArrayQueue:
    """Queue implementation using lists in python"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        '''Returns whether the queue is empty'''
        return len(self.items) == 0

    def enqueue(self, item):
        '''Admit the item into the queue'''
        # we add items towards the end of the list
        self.items.append(item)

    def peek(self):
        '''Return the item on the front of the queue without removing it'''
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        else:
            # while removing, we remove from first
            return self.items[0]

    def dequeue(self):
        '''Removes and returns the item at the front of the queue'''
        return self.items.pop(0)

    def display(self):
        '''Display the contents in the queue'''
        for item in self.items:
            print(item, end=" ")
        print()

    @property
    def size(self):
        '''Returns the size of the queue'''
        return len(self.items)


class LLQueue(LinkedList):
    """Implementation of queue using singly linked list"""

    def __init__(self):
        # initializing the super class, that is the linked list
        super().__init__()
        # creating a new property,  tail
        self.tail = None

    # the is_empty method that is defined on the linked list class
    # can be reused by inheritance, so no need to define here

    def enqueue(self, item):
        '''Admit the item into the queue'''
        # create a new node
        node = Node(item)
        if self.is_empty():
            # if the linked list is empty, the newly created node becomes head as well as tail
            self.head = self.tail = node
        else:
            # otherwise, add the node just after the tail
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        '''Removes and returns the item from the front of queue'''
        if self.is_empty():
            raise RuntimeError('Queue is empty')
        else:
            # remove the first item from the linked list
            data = self.remove_first()
            # after removal, if head becomes None, then we will know that the only node in the
            # linked list got deleted. so, we need to make tail equals None too
            if self.head is None:
                self.tail = None
            return data
