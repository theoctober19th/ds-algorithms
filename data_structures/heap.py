class MinHeap:
    """Implmentation of min heap in Python using array representation of binary tree"""

    def __init__(self, data=[]):
        # this array is used to hold the nodes
        self.nodes = []
        # constructing the heap using optimal algorithms
        self.construct_heap_optimal(data)

    def construct_heap_naive(self, data):
        """Naive algorithm to build the heap. Constructs the heap in O(n logn) time"""
        for node in data:
            # for every node in provided list, just keep on adding that data to the heap
            self.add(node)

    def construct_heap_optimal(self, data):
        """Optimal algorithm to construct a heap. This algorithm constructs the heap in O(n) time"""
        self.nodes = data
        n = len(data)
        # starting fromt the last non-leaf node, all the way back to root
        for i in range((n - 1) // 2, -1, -1):
            # perform sink operation (going downwards, and asserting heap invariant property)
            self.sink(i)

    def swim(self, i):
        """Move upwards towards the root from the node position i and recursively assert heap invariant property"""
        p = self.parent(i)
        # while we have not reached the heap node, and the heap invariant property is not satisfied
        # that means, the parent is grater than it's child
        while i != 0 and self.nodes[p] > self.nodes[i]:
            # swap the child with parent
            self.swap(i, p)
            # and move upwards towards the root
            i = p
            p = self.parent(i)

    def swap(self, i, j):
        """Swaps the values between two node positions i and j"""
        self.nodes[j], self.nodes[i] = self.nodes[i], self.nodes[j]

    def add(self, data):
        """Adds data into the heap. Works in O(logn) time."""
        # first of all, insert data as rightmost leaf node
        self.nodes.append(data)
        # now start swimming starting from this particular node
        self.swim(len(self.nodes) - 1)

    def pool(self):
        """ Remove an item from the heap and then return it """
        return self.delete(0)

    def delete(self, i):
        """Delete the node at position i, and then return it's value"""
        try:
            # find the rightmost leaf node
            last = len(self.nodes) - 1
            # swap it with the node to be deleted
            self.nodes[i], self.nodes[last] = self.nodes[last], self.nodes[i]
            # put aside data, for purpose of returning it later
            data = self.nodes.pop()
            # recursively sink towards the leaves
            self.sink()
            return data
        except Exception:
            # if the heap is empty
            raise RuntimeError('The heap is empty.')

    def sink(self, i=0):
        """ Go downwards in the heap and assert heap invariant property to all of the child."""
        l = self.child_left(i)
        r = self.child_right(i)
        # while l and r are within bounds
        while l < len(self.nodes) and r < len(self.nodes) and (self.nodes[i] > self.nodes[l] or self.nodes[i] > self.nodes[r]):
            if self.nodes[l] < self.nodes[r] or self.nodes[l] == self.nodes[r]:
                self.nodes[l], self.nodes[i] = self.nodes[i], self.nodes[l]
                i = l
            else:
                self.nodes[r], self.nodes[i] = self.nodes[i], self.nodes[r]
                i = r
            l = self.child_left(i)
            r = self.child_right(i)

    def print_heap(self):
        """Print the heap"""
        i, j = 0, 1
        for node in self.nodes:
            print(node, end="   ")
            if 2 ** j - 2 == i:
                print()
                j = j + 1
            i = i + 1
        print()

    def remove_naive(self, data):
        """Naive algorithm to remove an item 'data' from the heap"""
        try:
            # find the index of the node to be deleted
            i = self.nodes.index(data)
            last = len(self.nodes) - 1
            self.nodes[i], self.nodes[last] = self.nodes[last], self.nodes[i]
            self.nodes.pop()
            p = self.parent(i)
            if self.nodes[i] < self.nodes[p]:
                self.swim(i)
            else:
                self.sink(i)
        except ValueError:
            print("Element {} is not in the heap.".format(data))
        pass

    def child_left(self, idx):
        """Returns the left child position for given position"""
        return 2 * idx + 1

    def child_right(self, idx):
        """Returns the right child position for given position"""
        return 2 * idx + 2

    def parent(self, idx):
        """Returns the parent's position for given position"""
        return (idx - 1) // 2
