from circular_queue import CircularQueue


def main():
    queue = CircularQueue(size=5)
    queue.enqueue(99)
    queue.enqueue(34)
    # print(queue.items)
    queue.display()
    queue.enqueue(12)
    queue.dequeue()
    # queue.display()
    queue.enqueue(898)
    queue.enqueue(43)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()


if __name__ == "__main__":
    main()
