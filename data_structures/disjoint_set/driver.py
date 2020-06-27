from disjoint_set import DisjointSet


def main():
    ds = DisjointSet(["A", "B", "C", "D", "E"])
    ds.union("C", "A")
    ds.union("C", "D")
    print(ds.find("D"))


if __name__ == "__main__":
    main()
