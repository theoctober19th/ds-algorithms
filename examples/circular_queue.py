from data_structures.circular_queue import CircularQueue


def main():
    # creating a circular queue
    queue = CircularQueue(size=5)

    print('\nInserting a few items into the queue...')
    queue.enqueue(99)
    queue.enqueue(34)
    queue.display()

    print('\nInserting one more item into the queue...')
    queue.enqueue(12)
    queue.display()

    print('\nRemoving an item from the queue')
    queue.dequeue()
    queue.display()

    print('\nInserting a few items into the queue...')
    queue.enqueue(898)
    queue.enqueue(43)
    queue.display()

    print('\nRemoving a few items from the queue...')
    queue.dequeue()
    queue.dequeue()
    queue.display()


if __name__ == "__main__":
    main()
