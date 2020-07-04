class DisjointSet:
    """Implementation of disjoint set in Python"""

    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}
        self.num_sets = len(nodes)

    def find(self, node):
        '''Finds which set does a particular node belongs to'''
        # loop until the node is the parent of itself
        while self.parent[node] != node:
            node = self.parent[node]
        # return the node
        return node

    def union(self, node1, node2):
        ''''Performs the union operation between two sets node1 and node2'''
        # finding the sets to which node1 and node2 belong
        node1 = self.find(node1)
        node2 = self.find(node2)
        # make one of them a parent of other
        if self.size[node1] < self.size[node2]:
            self.parent[node1] = node2
            self.size[node1] = self.size[node1] + self.size[node2]
        else:
            self.parent[node2] = node1
            self.size[node2] = self.size[node1] + self.size[node2]
        self.num_sets = self.num_sets - 1
