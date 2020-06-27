from bst import BinarySearchTree


def main():
    data = [17, 13, 10, 15, 4, 11, 16, 21, 24, 23, 27, 25, 26]
    bst = BinarySearchTree(data)
    print(bst.breadth_first_list())
    bst.remove(4)
    bst.remove(10)
    bst.remove(27)
    bst.remove(13)
    print(bst.breadth_first_list())
    bst.add(45)
    print(bst.breadth_first_list())
    print(bst.height())
    print(bst.contains(45))


if __name__ == "__main__":
    main()
