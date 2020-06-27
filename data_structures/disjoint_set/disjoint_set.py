class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}
        self.num_sets = len(nodes)

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if self.size[node1] < self.size[node2]:
            self.parent[node1] = node2
            self.size[node1] = self.size[node1] + self.size[node2]
        else:
            self.parent[node2] = node1
            self.size[node2] = self.size[node1] + self.size[node2]
        self.num_sets = self.num_sets - 1

