from data_structures.stack import Stack
from data_structures.queue import ArrayQueue as Queue


class Node:
    """A node for a binary search tree"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        '''Returns whether the node is a leaf node or not'''
        return self.left is None and self.right is None


class BinarySearchTree:
    """Python implementation of a Binary Search Tree"""

    def __init__(self, data=[]):
        self.root = None
        self.num_nodes = 0
        # for each item in the given list, gradually add the item to the BST
        for item in data:
            self.add(item)

    @property
    def size(self):
        '''Returns the size of the binary search tree'''
        return self.num_nodes

    @property
    def height(self):
        '''Returns the height of the tree'''
        return self.height_recursive(self.root)

    def height_recursive(self, node):
        '''Recursively computes the height of the BST'''
        if node is None:
            return 0
        return max(self.height_recursive(node.left), self.height_recursive(node.right)) + 1

    def add(self, item):
        '''Adds an item to the BST'''
        self.root = self.add_recursive(self.root, item)
        self.num_nodes = self.num_nodes + 1

    def add_recursive(self, node, item):
        '''Recursively adds an item to the node 'node' in the BST'''
        if node is None:
            node = Node(item)
        elif item <= node.data:
            # in this case, recursively construct the left subtree
            node.left = self.add_recursive(node.left, item)
        else:
            # in this case, recursively construct the right sub tree
            node.right = self.add_recursive(node.right, item)
        return node

    def in_order_recursive(self, node, li):
        """Recursively traverse the BST in 'in-order' strategy"""
        if not node:
            return li
        self.in_order_recursive(node.left, li)
        li.append(node.data)
        self.in_order_recursive(node.right, li)
        return li

    def pre_order_recursive(self, node, li):
        """Recursively traverse the BST in 'pre-order' strategy"""
        if not node:
            return li
        li.append(node.data)
        self.pre_order_recursive(node.left, li)
        self.pre_order_recursive(node.right, li)
        return li

    def post_order_recursive(self, node, li):
        """Recursively traverse the BST in 'post-order' strategy"""
        if not node:
            return li
        self.post_order_recursive(node.left, li)
        self.post_order_recursive(node.right, li)
        return li

    def depth_first_list(self):
        """returns a list created by traversing the tree in depth first manner"""
        li = []
        stack = Stack("bst")
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.pop()
            li.append(node.data)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
        return li

    def breadth_first_list(self):
        """Returns a list created by traversing the tree in breadth first manner"""
        li = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            li.append(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return li

    def pre_order_list(self):
        """Returns a list created by traversing the tree in 'pre-order' manner"""
        return self.pre_order_recursive(self.root, [])

    def in_order_list(self):
        """Returns a list created by traversing the tree in 'in-order' manner"""
        return self.in_order_recursive(self.root, [])

    def post_order_list(self):
        """Returns a list created by traversing the tree in 'post-order' manner"""
        return self.pre_order_recursive(self.root, [])

    def find_max_in_left_subtree(self, node):
        """Finds and returns the node that has the maximum value on the left subtree of 'node'"""
        node = node.left
        while not node.is_leaf():
            node = node.right
        return node

    def find(self, item):
        '''Finds and returns the node that contains a particular item'''
        node = self.root
        while node != None:
            if node.data == item:
                return node
            elif node.data < item:
                node = node.right
            else:
                node = node.left
        return None

    def contains(self, item):
        '''Returns if the BST contains a particular item'''
        return self.find(item) != None

    def remove_recursive(self, node, item):
        '''Recursively remove an item from the BST'''
        if node is None:
            return None
        if item < node.data:
            node.left = self.remove_recursive(node.left, item)
        elif item > node.data:
            node.right = self.remove_recursive(node.right, item)
        else:
            if node.left is None:
                right_child = node.right
                node.data = None
                node = None
                return right_child
            elif node.right is None:
                left_child = node.left
                node.data = None
                node = None
                return left_child
            else:
                temp = self.find_max_in_left_subtree(node)
                node.data = temp.data
                node.left = self.remove_recursive(node.left, temp.data)
        return node

    def remove(self, item):
        '''Removes an item from the BST'''
        node = self.find(item)
        if not node:
            raise RuntimeError('Value doesn\'t exist in the tree')
        else:
            self.root = self.remove_recursive(self.root, item)
            self.num_nodes = self.num_nodes - 1
