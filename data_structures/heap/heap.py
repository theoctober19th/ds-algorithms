class MinHeap:
    def __init__(self, data=[]):
        self.nodes = []
        self.construct_heap_optimal(data)

    def construct_heap_naive(self, data):
        for node in data:
            self.add(node)

    def construct_heap_optimal(self, data):
        self.nodes = data
        n = len(data)
        for i in range((n - 1) // 2, -1, -1):
            self.sink(i)

    def swim(self, i):
        p = self.parent(i)
        while i != 0 and self.nodes[p] > self.nodes[i]:
            self.swap(i, p)
            i = p
            p = self.parent(i)

    def swap(self, i, j):
        self.nodes[j], self.nodes[i] = self.nodes[i], self.nodes[j]

    def add(self, data):
        self.nodes.append(data)
        self.swim(len(self.nodes) - 1)

    def pool(self):
        return self.delete(0)

    def delete(self, i):
        try:
            last = len(self.nodes) - 1
            self.nodes[i], self.nodes[last] = self.nodes[last], self.nodes[i]
            data = self.nodes.pop()
            self.sink()
            return data
        except Exception:
            print("Heap is empty.")
            return None

    def sink(self, i=0):
        l = self.child_left(i)
        r = self.child_right(i)
        # while l and r are within bounds
        while (
            l < len(self.nodes)
            and r < len(self.nodes)
            and (self.nodes[i] > self.nodes[l] or self.nodes[i] > self.nodes[r])
        ):
            if self.nodes[l] < self.nodes[r] or self.nodes[l] == self.nodes[r]:
                self.nodes[l], self.nodes[i] = self.nodes[i], self.nodes[l]
                i = l
            else:
                self.nodes[r], self.nodes[i] = self.nodes[i], self.nodes[r]
                i = r
            l = self.child_left(i)
            r = self.child_right(i)

    def print_heap(self):
        i, j = 0, 1
        for node in self.nodes:
            print(node, end="   ")
            if 2 ** j - 2 == i:
                print()
                j = j + 1
            i = i + 1
        print()

    def remove_naive(self, data):
        try:
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
        return 2 * idx + 1

    def child_right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return (idx - 1) // 2

