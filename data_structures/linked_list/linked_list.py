class Node:
    def __init__(self, key=None, payload=None):
        self.key = key
        self.next = None
        self.payload = None

    def __str__(self):
        return 'Node with key:{}'.format(self.key)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, key, payload=None):
        if self.head:
            trav = self.head
            while trav.next != None:
                trav = trav.next
            trav.next = Node(key, payload)
        else:
            self.head = Node(key)

    def insert_first(self, key, payload=None):
        node = Node(key, payload)
        if self.head:
            node.next = self.head
        self.head = node

    def find_node(self, key):
        trav = self.head
        while trav != None:
            if trav.key == key:
                return trav
            trav = trav.next
        return None

    def insert_after(self, after, key, payload=None):
        node = self.find_node(after)
        if node:
            new_node = Node(key, payload)
            new_node.next = node.next
            node.next = new_node
        else:
            return RuntimeError("Did not found {} in the list.".format(after))

    def remove_first(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def remove_last(self):
        trav = self.head
        if self.head.next == None:
            self.head = None
            return
        else:
            while trav.next.next != None:
                trav = trav.next
            trav.next = None

    def remove(self, key):
        trav = self.head
        if self.head != None and self.head.key == key:
            self.head = self.head.next
            return
        else:
            while trav.next.next != None and trav.next.key != key:
                trav = trav.next
            if trav.next.key == key:
                trav.next = trav.next.next

    def display(self):
        trav = self.head
        while trav != None:
            print(trav.key, end=' ')
            trav = trav.next
            if trav:
                print('->', end=' ')
        print()

    def size(self):
        trav = self.head
        count = 0
        while trav != None:
            count = count + 1
            trav = trav.next
        return count
