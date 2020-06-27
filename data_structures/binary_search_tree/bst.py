from data_structures.stack.stack import Stack
from data_structures.queue.queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


class BinarySearchTree:
    def __init__(self, data=[]):
        self.root = None
        self.num_nodes = 0
        for item in data:
            self.add(item)

    def size(self):
        return self.num_nodes

    def height(self):
        return self.height_recursive(self.root)

    def height_recursive(self, node):
        if node is None:
            return 0
        return max(self.height_recursive(node.left), self.height_recursive(node.right)) + 1

    def add(self, item):
        self.root = self.add_recursive(self.root, item)
        self.num_nodes = self.num_nodes + 1

    def add_recursive(self, node, item):
        if node == None:
            node = Node(item)
        elif item <= node.data:
            node.left = self.add_recursive(node.left, item)
        else:
            node.right = self.add_recursive(node.right, item)
        return node

    def in_order_recursive(self, node, li):
        if not node:
            return li
        self.in_order_recursive(node.left, li)
        li.append(node.data)
        self.in_order_recursive(node.right, li)
        return li

    def pre_order_recursive(self, node, li):
        if not node:
            return li
        li.append(node.data)
        self.pre_order_recursive(node.left, li)
        self.pre_order_recursive(node.right, li)
        return li

    def post_order_recursive(self, node, li):
        if not node:
            return li
        self.post_order_recursive(node.left, li)
        self.post_order_recursive(node.right, li)
        return li

    def depth_first_list(self):
        li = []
        stack = Stack("bst")
        stack.push(self.root)
        while not stack.empty():
            node = stack.pop()
            li.append(node.data)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
        return li

    def breadth_first_list(self):
        li = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.empty():
            node = queue.dequeue()
            li.append(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return li

    def pre_order_list(self):
        return self.pre_order_recursive(self.root, [])

    def in_order_list(self):
        return self.in_order_recursive(self.root, [])

    def post_order_list(self):
        return self.pre_order_recursive(self.root, [])

    def find_max_in_left_subtree(self, node):
        node = node.left
        while not node.is_leaf():
            node = node.right
        return node

    def find(self, item):
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
        return self.find(item) != None

    def remove_recursive(self, node, item):
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

        # if rootnode.data < nodetoremove.data:
        #     rootnode = self.remove_recursive(rootnode.right, nodetoremove)
        # elif rootnode.data > nodetoremove.data:
        #     rootnode = self.remove_recursive(rootnode.left, nodetoremove)
        # elif rootnode.data == nodetoremove.data:
        #     if nodetoremove.is_leaf():
        #         rootnode = None
        # return rootnode

    def remove(self, item):
        node = self.find(item)
        if not node:
            raise RuntimeError('Value doesn\'t exist in the tree')
        else:
            self.root = self.remove_recursive(self.root, item)
            self.num_nodes = self.num_nodes - 1
