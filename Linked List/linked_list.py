class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        if self.head:
            trav = self.head
            while trav.next != None:
                trav = trav.next
            trav.next = Node(data)
        else:
            self.head = Node(data)

    def insert_first(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node

    def find_node(self, data):
        trav = self.head
        while trav != None:
            if trav.data == data:
                return trav
            trav = trav.next
        return None

    def insert_after(self, after, data):
        node = self.find_node(after)
        if node:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
        else:
            return RuntimeError('Did not found {} in the list.'.format(after))

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

    def remove(self, data):
        trav = self.head
        if self.head != None and self.head.data == data:
            self.head = self.head.next
            return
        else:
            while trav.next.next != None and trav.next.data != data:
                trav = trav.next
            if trav.next.data == data:
                trav.next = trav.next.next

    def display(self):
        trav = self.head
        while trav != None:
            print(trav.data, end=' ')
            trav = trav.next
        print()

    def size(self):
        trav = self.head
        count = 0
        while trav != None:
            count = count + 1
            trav = trav.next
        return count


def main():
    animals = LinkedList()
    animals.insert_last('Dog')
    animals.insert_last('Cat')
    animals.insert_last('Horse')
    animals.insert_after('Dog', 'Giraffe')
    animals.insert_first('Apple')
    animals.display()

    animals.remove('Apple')
    animals.display()
    print('List contains {} elements.'.format(animals.size()))


if __name__ == '__main__':
    main()
