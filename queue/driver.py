from queue import Queue


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


if __name__ == "__main__":
    main()
