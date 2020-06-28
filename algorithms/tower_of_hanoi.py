from data_structures.stack.stack import Stack


class TowerOfHanoi:
    def __init__(self):
        self.pegA = Stack("A")
        self.pegB = Stack("B")
        self.pegC = Stack("C")

    def init_discs(self, n=3):
        for i in range(n, 0, -1):
            self.pegA.push(i)

    def transfer(self, frm, to, via, n):
        if n == 1:
            el = frm.pop()
            to.push(el)
            print("{} moved from {} to {}".format(el, frm.name, to.name))
        else:
            self.transfer(frm=frm, to=via, via=to, n=n - 1)
            self.transfer(frm, to, via, n=1)
            self.transfer(frm=via, to=to, via=frm, n=n - 1)

    def start(self):
        self.transfer(self.pegA, self.pegC, self.pegB, self.pegA.size())


def main():
    toh = TowerOfHanoi()
    toh.init_discs()
    toh.start()


if __name__ == "__main__":
    main()
