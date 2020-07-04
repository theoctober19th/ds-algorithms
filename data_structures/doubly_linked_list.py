class Node:
    """The node of a doubly linked list"""

    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def is_empty(self):
        '''Returns  whether the doubly linked list is empty'''
        return self.head == self.tail == None

    def insert_front(self, item):
        '''Insert the given item at the front of doubly linked list'''
        node = Node(item)
        if self.is_empty():
            # create a new node, this new node is both head as well as tail
            self.head = node
            self.tail = node
        else:
            # new nodes next pointer will be pointing to exisiting head
            node.next = self.head
            # exisiting head's pointer will be pointing back to the new node
            self.head.prev = node
            self.head = node
        self.num_items = self.num_items + 1

    def insert_back(self, item):
        '''Insert item at the end of the doubly linked list'''
        node = Node(item)
        if self.is_empty():
            # create a new node, this new node is both head as well as tail
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.num_items = self.num_items + 1

    def remove_front(self):
        '''Remove and return the item at the front of doubly linked list'''
        if self.is_empty():
            raise RuntimeError('Linked list is empty!')
        # else if list has only one node
        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.num_items = self.num_items - 1
            return data
        else:
            data = self.head.data
            self.head.next.prev = None
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.num_items = self.num_items - 1
            return data

    def remove_back(self):
        '''Remove and return the item at the end of doubly linked list'''
        if self.is_empty():
            raise RuntimeError('Linked list is empty!')
        # else if list has only one node
        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.num_items = self.num_items - 1
            return data
        else:
            data = self.tail.data
            self.tail.prev.next = None
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.num_items = self.num_items - 1
            return data

    def display(self):
        '''Display the doubly linked list'''
        trav = self.head
        while trav is not None:
            print(trav.data, end=' ')
            trav = trav.next
            if trav is not None:
                print('->', end=' ')
        print()

    def insert_after(self, item1, item2):
        '''inserts item2 after item1 in the linked list'''
        if self.tail.data == item1:
            # the item1 lies on the tail
            self.insert_back(item2)
        else:
            trav = self.head
            while trav is not None:
                if trav.data == item1:
                    # item1 is found, we need to insert item2 after it now
                    node = Node(item2)
                    trav.next.prev = node
                    node.next = trav.next
                    trav.next = node
                    node.prev = trav
                    self.num_items = self.num_items + 1
                    # return from this  method as we already have inserted the node
                    return
                trav = trav.next
            raise RuntimeError(f'The key {item1} does not exist in the list.')

    def remove(self, item):
        '''Removes the specified item from the linked list'''
        if self.is_empty():
            raise RuntimeError('The list is empty.')
        elif self.head == self.tail:
            self.head = self.tail = None
            self.num_items = self.num_items + 1
            return
        elif self.head.data == item:
            # if the item to be deleted is on the head node,
            self.remove_front()
            return
        elif self.tail.data == item:
            # if the item to be deleted is on the tail node,
            self.remove_back()
            return
        else:
            trav = self.head
            while trav is not None:
                if trav.data == item:
                    # the item is found
                    trav.next.prev = trav.prev
                    trav.prev.next = trav.next
                    self.num_items = self.num_items - 1
                    return
                trav = trav.next
            raise RuntimeError(
                'The item {} does not exist in the list'.format(item))

    @property
    def size(self):
        return self.num_items
