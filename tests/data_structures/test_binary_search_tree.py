# these tests are written for pytest module
# to run these tests, simply do: pytest test_binary_search_tree.py

from data_structures.binary_search_tree import BinarySearchTree


def test_empty():
    bst = BinarySearchTree()
    assert bst.size == 0
    assert bst.root is None


def test_insertion():
    bst = BinarySearchTree()
    bst.add(22)
    assert bst.size == 1
    assert bst.root.data == 22
    assert bst.root.left is None
    assert bst.root.right is None
    bst.add(56)
    bst.add(13)
    assert bst.root.right.data == 56
    assert bst.root.left.data == 13
    assert bst.size == 3


def test_removal():
    bst = BinarySearchTree()

    bst.add(2)
    bst.add(4)
    bst.add(55)
    assert bst.size == 3
    bst.remove(4)
    assert bst.size == 2
    assert bst.root.right.data == 55


def test_contains():
    bst = BinarySearchTree([5, 7, 3])
    assert bst.contains(5) == True
    assert bst.contains(99) == False
