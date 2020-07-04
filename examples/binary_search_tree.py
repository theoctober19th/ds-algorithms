from data_structures.binary_search_tree import BinarySearchTree


def main():
    # creating a binary search tree
    data = [17, 13, 10, 15, 4, 11, 16, 21, 24, 23, 27, 25, 26]
    bst = BinarySearchTree(data)
    print(bst.breadth_first_list())

    # Removing a few items...
    print('\nDeleting a few items...')
    bst.remove(4)
    bst.remove(10)
    bst.remove(27)
    bst.remove(13)
    print(bst.breadth_first_list())

    print("\nadding 45 to BST...")
    bst.add(45)
    print(bst.breadth_first_list())

    print('\nTHe height of the tree :', bst.height)

    print('\nBST contains 45:', bst.contains(45))


if __name__ == "__main__":
    main()
