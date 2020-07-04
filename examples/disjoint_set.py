from data_structures.disjoint_set import DisjointSet


def main():
    # creating a disjoint set
    ds = DisjointSet(["A", "B", "C", "D", "E"])
    # performing some union operations
    ds.union("C", "A")
    ds.union("C", "D")
    # performing a find operation
    print(ds.find("D"))


if __name__ == "__main__":
    main()
