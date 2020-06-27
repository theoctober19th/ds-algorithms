class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def peek(self):
        if self.empty():
            raise RuntimeError("Queue is empty")
        else:
            return self.items[0]

    def dequeue(self):
        return self.items.pop(0)

    def display(self):
        for item in self.items:
            print(item, end=" ")
        print()

