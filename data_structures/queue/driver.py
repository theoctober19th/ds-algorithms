from queue import Queue, QueueOptimal


def main():
    queue = Queue()
    queue.enqueue(99)
    queue.enqueue(34)
    queue.enqueue(12)
    queue.enqueue(54)
    queue.enqueue(898)
    queue.enqueue(43)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()

    # optimal queue using linked list
    print('\nOptimal queue using linked list')
    q = QueueOptimal()
    # q.display()
    q.enqueue(34)
    q.enqueue(56)
    q.enqueue(67)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.display()


if __name__ == "__main__":
    main()
