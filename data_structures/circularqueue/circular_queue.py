class CircularQueue():
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head = 0
        self.tail = 0

    @property
    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.max_size - (self.head - self.tail)

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            raise RuntimeError('The queue is full.')
        else:
            self.items[self.tail] = item
            self.advance_tail()

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('The queue is empty')
        else:
            item = self.items[self.head]
            self.advance_head()
            return item

    def advance_head(self):
        self.head = (self.head + 1) % self.max_size

    def advance_tail(self):
        self.tail = (self.tail + 1) % self.max_size

    def display(self):
        h = self.head
        while h != self.tail:
            print(self.items[h], end=' ')
            h = (h + 1) % self.max_size
        print()
