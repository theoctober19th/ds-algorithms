from data_structures.linked_list import LinkedList
from collections import namedtuple
import math
# python has builtin dictionary data type
# which is an optimized implementation of hashtable
# but i have tried to implement hashtable from scratch
# just so we know how it works

Entry = namedtuple('Entry', ['key', 'value'])


class HashTable:
    """Manual simulation of hash table in Python where hash collisions are resolved by separate chaining"""

    def __init__(self, size, hash_func, threshold_factor=0.8):
        """
        Params:
            size: The size of the hash table array
            hash_func: The function which will calculate the hash when key is provided
            threshold_factor: The load factor when exceeded we should extend the size of table
        """
        self.size = size
        self.num_items = 0
        self.filled_buckets = 0
        # create a table of linked lists of size 'size'
        self.table = [LinkedList() for i in range(size)]
        self.hash_func = hash_func
        self.threshold_factor = threshold_factor

    def compute_hash(self, key):
        '''Calculates the hash of a given key'''
        return self.hash_func(key) % self.size

    def insert(self, key, value):
        '''Inserts the key and the payload into the hash tale'''
        # first of all, compute hash of the key
        i = self.compute_hash(key)
        # now find the bucket it should be stored on
        bucket = self.table[i]
        # if the bucket is empty
        if bucket.head == None:
            # increment the number of filled buckets
            self.filled_buckets = self.filled_buckets + 1
        # create a key value pair and insert at the last of the linked list
        item = Entry(key=key, value=value)
        bucket.insert_back(item)
        # increment the number of items
        self.num_items = self.num_items + 1
        # if the number of filled buckets exceeds the load factor, then resize the hashtable
        if self.filled_buckets > self.size * self.threshold_factor:
            self.resize()

    def resize(self):
        '''Resizes the hashtable to double its present size'''
        # copy and keep backup of the existing table
        oldtable = self.table.copy()
        # double the size of hashtable
        self.size = self.size * 2
        # create a new table with twice the number of linked lists
        self.table = [LinkedList() for i in range(self.size)]
        self.num_items = 0
        self.filled_buckets = 0
        # rehash every keys in the old hash table
        self.rehash(oldtable)

    def rehash(self, oldtable):
        '''Rehashes all the keys stored in oldtable'''
        # for each bucket in the old table
        for bucket in oldtable:
            trav = bucket.head
            # for each node in particular bucket
            while trav is not None:
                # insert the key and payload into the new hashtable
                self.insert(trav.key, trav.value)
                trav = trav.next

    def display(self):
        '''Displays the contents in the hashtable'''
        for index, bucket in enumerate(self.table):
            print('Bucket', index, end=': ')
            # calling display method of the linked list
            bucket.display()
        print()

    def get(self, key):
        '''Returns the value associated with a particular key'''
        item = self.find(key)
        if item is None:
            raise RuntimeError('The key does not exist.')
        else:
            return item.value

    def find(self, key):
        '''Finds a particular key in the hashtable and returns the key, value pair if exists'''
        index = self.compute_hash(key)
        bucket = self.table[index]
        trav = bucket.head
        while trav != None:
            if trav.data.key == key:
                return trav.data
            trav = trav.next
        return None

    def contains(self, key):
        '''Returns whether the hashtable contains a particular key'''
        return True if self.find(key) is not None else False

    def remove(self, key):
        '''Removes a particular key from the hashtable'''
        item = self.find(key)
        if item is not None:
            index = self.compute_hash(key)
            bucket = self.table[index]
            # calling remove method of the linked list
            bucket.remove(item)
        else:
            raise RuntimeError('The key does not exist in the hashtable.')

    def get(self, key):
        '''Get the value assiciated with the given key'''
        node = find(key)
        if node is None:
            raise RuntimeError('Key does not exist.')
        else:
            return node
