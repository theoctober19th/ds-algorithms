class CircularQueue():
    '''Implementation of fixed size circular queue in Python, using list'''

    def __init__(self, size):
        """
        Params:
            size: The maximum size of the circular queue to be constructed
        """
        self.items = [0] * size
        self.max_size = size
        self.head = 0
        self.tail = 0

    @property
    def size(self):
        '''Returns the number of items currently in the queue'''
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.max_size - (self.head - self.tail)

    def is_full(self):
        '''Returns whether the queue is full'''
        return self.size == self.max_size

    def is_empty(self):
        '''Returns whether the queue is empty'''
        return self.size == 0

    def enqueue(self, item):
        '''Inserts the item into the queue'''
        if self.is_full():
            raise RuntimeError('The queue is full.')
        else:
            self.items[self.tail] = item
            self.advance_tail()

    def dequeue(self):
        '''Removes an item from the queue and returns it'''
        if self.is_empty():
            raise RuntimeError('The queue is empty')
        else:
            item = self.items[self.head]
            self.advance_head()
            return item

    def advance_head(self):
        '''Move the head pointer one position further'''
        self.head = (self.head + 1) % self.max_size

    def advance_tail(self):
        '''Move the tail pointer one position further'''
        self.tail = (self.tail + 1) % self.max_size

    def display(self):
        '''Display the items in the queue'''
        h = self.head
        while h != self.tail:
            print(self.items[h], end=' ')
            # advancing the pointer h one position further
            h = (h + 1) % self.max_size
        print()
