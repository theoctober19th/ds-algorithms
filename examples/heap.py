from data_structures.heap import MinHeap


def main():
    # creating a heap
    heap = MinHeap([6, 7, 4, 2, 5, 7, 8, 12, 23, 1, 43, 6, 0])

    # printing the heap
    heap.print_heap()

    print('\n Adding a few elements...')
    heap.add(21)
    heap.add(87)
    heap.print_heap()

    print('\n Pooling from the heap...')
    print(heap.pool())

    print('Remove item 21 from the heap')
    heap.remove_naive(23)
    heap.print_heap()


if __name__ == "__main__":
    main()
