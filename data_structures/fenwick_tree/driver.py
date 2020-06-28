from fenwick import FenwickTree


def main():
    data = [5, 2, 7, 9, 3, 4, 6, 8]
    # construction
    tree = FenwickTree(data)
    tree.display()

    # prefix sum query
    print(tree.prefix_sum(upto=6))

    # range sum query
    print(tree.range_sum(frm=3, to=7))

    # update
    tree.update(3, 88)
    tree.display()


if __name__ == "__main__":
    main()
