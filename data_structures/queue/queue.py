from data_structures.linked_list.linked_list import LinkedList, Node


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


class QueueOptimal(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def empty(self):
        return self.head == self.tail == None

    def enqueue(self, item):
        node = Node(item)
        if self.empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.empty():
            raise RuntimeError('Queue is empty')
        else:
            data = self.remove_first()
            if self.head == None:
                self.tail = None
            return data
