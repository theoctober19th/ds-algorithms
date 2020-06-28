from typing import List


class FenwickTree:
    def __init__(self, items: List):
        self.tree = items.copy()
        self.tree.insert(0, 0)
        self.populate()

        self.tree = [0] * (len(items) + 1)
        for idx, item in enumerate(items):
            self.update(idx + 1, item)

    def populate(self):
        for i in range(1, len(self.tree)):
            p = i + (i & -i)
            try:
                self.tree[p] = self.tree[p] + self.tree[i]
            except:
                pass

    def size(self):
        return len(self.tree)

    def update(self, index: int, amount: int):
        while index < self.size():
            self.tree[index] = self.tree[index] + amount
            index = index + (index & -index)

    def display(self):
        for i in range(1, len(self.tree)):
            print(self.tree[i], end=', ')
        print()

    def prefix_sum(self, upto: int):
        res = 0
        while upto > 0:
            res = res + self.tree[upto]
            upto = upto - (upto & -upto)
        return res

    def range_sum(self, frm: int, to: int):
        return self.prefix_sum(to) - self.prefix_sum(frm-1)
