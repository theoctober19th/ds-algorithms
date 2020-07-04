import unittest
from data_structures.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.items = DoublyLinkedList()

    # test for empty linked list
    def test_empty_list(self):
        self.assertEqual(self.items.head, None)
        self.assertEqual(self.items.tail, None)

    # Tests forbidden operations like removal in a empty linked list
    def test_forbidden_operations_on_empty_linked_list(self):
        self.assertEqual(self.items.size, 0)
        with self.assertRaises(RuntimeError):
            self.items.remove_back()
        with self.assertRaises(RuntimeError):
            self.items.remove_front()

    def test_delete_nonexistent_item(self):
        self.items.insert_back('A')
        self.items.insert_front('B')
        with self.assertRaises(RuntimeError):
            self.items.remove('Z')

    def test_insert_back(self):
        self.items.insert_back('Z')
        self.assertEqual(self.items.size, 1)
        self.assertEqual(self.items.remove_back(), 'Z')
        self.items.insert_back('Y')
        self.items.insert_back('T')
        self.items.insert_back('E')
        self.assertEqual(self.items.remove_front(), 'Y')

    def test_insert_front(self):
        self.items.insert_front('A')
        self.assertEqual(self.items.size, 1)
        self.assertEqual(self.items.remove_front(), 'A')
        self.items.insert_front('B')
        self.items.insert_front('C')
        self.items.insert_front('D')
        self.assertEqual(self.items.remove_back(), "B")
        self.assertEqual(self.items.remove_front(), "D")

    def test_remove(self):
        with self.assertRaises(RuntimeError):
            self.items.remove('T')
        self.items.insert_front('T')
        self.items.insert_back('R')
        self.items.insert_after('R', 'Y')
        self.items.remove('R')
        self.assertEqual(self.items.size, 2)
        self.assertEqual(self.items.remove_back(), 'Y')
        self.assertEqual(self.items.size, 1)
        self.items.remove_front()
        self.assertEqual(self.items.size, 0)
        with self.assertRaises(RuntimeError):
            self.items.remove_front()

    # when only one node is there
    def test_single_node_case(self):
        self.items.insert_front(1)
        self.items.remove_front()
        self.assertEqual(self.items.head, self.items.tail)


if __name__ == "__main__":
    unittest.main()
