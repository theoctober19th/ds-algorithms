class Node:
    '''A node in the linked list'''

    def __init__(self, item):
        """
        Args:
            item: The item to be inserted
        """
        self.data = item
        self.next = None

    # string representation of this node
    def __str__(self):
        return self.data


class LinkedList:
    """Implementation of a singly linked list in Python"""

    def __init__(self):
        self.head = None
        self.num_items = 0

    def is_empty(self):
        '''Returns whether the linked list is empty'''
        return self.head is None

    def insert_back(self, item):
        """Inserts an item at the end of the linked list.

        Args:
            item: The item to be inserted
        """
        # creating a new node with key and payload
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            trav = self.head
            # reach to the last node in the list
            while trav.next is not None:
                trav = trav.next
            # existing last node points its next pointer to the newly created node
            trav.next = node
        self.num_items = self.num_items + 1

    def insert_front(self, item):
        """Insert an item at the beginning of the linked list.

        Args:
            item: The item to be inserted
        """
        # create a new node along with given key and payload
        node = Node(item)
        node.next = self.head
        self.head = node
        self.num_items = self.num_items + 1

    def insert_after(self, after, item):
        """Insert an item after a particular item in the linked list.

        Args:
            after: The item after which the new new item is to be inserted
            item: The item to be inserted
        """
        trav = self.head
        # traverse till the end of the list is reached
        while trav is not None:
            # if the key of an intermediate node is equal to key provided, break
            if trav.data == after:
                break
            # else, proceed to next node
            trav = trav.next
        # check if the key inside trav node is actually the key we are searching for
        if trav.data != after:
            # means 'after' is not found in the list.
            raise RuntimeError(f'The item {after} does not exist in the list.')
        else:
            # create a node and insert it just after trav
            node = Node(item)
            node.next = trav.next
            trav.next = node
            self.num_items = self.num_items + 1

    def update(old_item, new_item):
        """Updates an item with a new value.

        Args:
            key: The key of the node to be updated
            payload: The payload to be updated inside the node
        """
        trav = self.head
        # until we traverse all the nodes
        while trav is not None:
            # if the key is found
            if trav.data == old_item:
                # udpate the payload
                trav.data = new_item
                break

    def remove_first(self):
        """Removes and returns the first item in the list

        Returns:
            The first item in the list.
        """
        if self.is_empty():
            raise RuntimeError('The list is empty.')
        else:
            data = self.head
            self.head = self.head.next
            # decrease count by one
            self.num_items = self.num_items - 1
            return data

    def remove_last(self):
        """Removes and returns the last item in the list

        Returns:
            The last item in the list.
        """
        if self.is_empty():
            raise RuntimeError('THe list is empty.')
        # if there is only one node in the list
        elif self.head.next is None:
            data = self.head.data
            self.head = self.head.next
            self.num_items = self.num_items - 1
            return data

        # if there are more than one node
        else:
            trav = self.head
            # reach to the second last node
            while trav.next.next is not None:
                trav = trav.next
            # take out the data from the last node in order to return it later
            data = trav.next.data
            trav.next = None
            self.num_items = self.num_items - 1
            return data

    def remove(self, item):
        """Removes an item from the list.

        Args:
            item: The item to be deleted
        """
        # check if the list is empty:
        if self.is_empty():
            raise RuntimeError('The list is empty.')
        # check if the key to be removed is on the head
        if self.head.data == item:
            # in that case, simply make the head point to head.next and return the payload
            data = self.head.data
            self.head = self.head.next
            self.num_items = self.num_items - 1
            return data
        else:
            trav = self.head
            # while we have not reached either the last node
            # or the node just before the node to be removed
            while trav.next is not None and trav.next.data != item:
                trav = trav.next

            if trav.next is None:
                # we have reached the end of the list
                # and we did not found the key
                raise RuntimeError('The key does not exist in the list.')
            else:
                # we have found the key, and we are at a node just before the node containing key
                data = trav.next.data
                trav.next = trav.next.next
                self.num_items = self.num_items - 1
                return data

    def display(self):
        """Prints the contents of a list in sequential order."""
        trav = self.head
        # loop for every node
        while trav is not None:
            print(trav.data, end=' ')
            trav = trav.next
            # if there exists next node, print an arrow
            if trav is not None:
                print('->', end=' ')
        # print a new line at the end
        print()

    @property
    def size(self):
        '''Returns the size of the linked list'''
        return self.num_items
