from data_structures.linked_list import LinkedList
from collections import namedtuple
import math
# python has builtin dictionary data type
# which is an optimized implementation of hashtable
# but i have tried to implement hashtable from scratch
# just so we know how it works

Entry = namedtuple('Entry', ['key', 'value'])


class HashTable:
    """Manual simulation of hash table in Python where hash collisions are resolved by probing"""
    # this defines a zombie Entry. A Entry becomes zombie after it is deleted
    # it can't be directly deleted because we still may need this particular entry to probe to later entries
    ZOMBIE = Entry(key=None, value=None)

    def __init__(self, size, hash_func, probe_func, threshold_factor=0.66):
        """
        Params:
            size: The size of the hash table array
            hash_func: The function which will calculate the hash when key is provided
            probe_func: The function that will calculate the offset from hash to probe at a particular instant
            threshold_factor: The load factor when exceeded we should extend the size of table
        """
        self.size = size
        self.num_items = 0
        # create a table of size 'size'
        self.table = [None for i in range(size)]
        self.hash_func = hash_func
        self.probe_func = probe_func
        self.threshold_factor = threshold_factor

    def compute_hash(self, key):
        '''Computes the hash of a key'''
        return self.hash_func(key) % self.size

    def compute_probe(self, probe, key):
        '''Computes the probing offset for the provided value of probe'''
        return self.probe_func(probe, key, self.size)

    def display(self):
        '''Display the hahtable'''
        for item in self.table:
            if item is None:
                print(item, end=' ')
            # if item is a zombie
            elif item is HashTable.ZOMBIE:
                print('ZOMBIE', end=' ')
            else:
                print(item.value, end=' ')
        print()

    def insert(self, key, value):
        '''Insert into the hashtable'''
        x = 0
        # compute the hash of the key
        h = self.compute_hash(key)
        probed_hash = (h + self.compute_probe(x, key)) % self.size
        # until we reach an empty slot, keep probing
        while self.table[probed_hash] is not None and self.table[probed_hash] != HashTable.ZOMBIE:
            x = x + 1
            probed_hash = (h + self.compute_probe(x, key)) % self.size
        # insert the (key, value) tuple at this position
        self.table[probed_hash] = Entry(key=key, value=value)
        self.num_items = self.num_items + 1
        # if number of items exceed threshold factor, resize the hashtable
        if self.num_items > self.threshold_factor * self.size:
            self.resize()

    def resize(self):
        '''Resizes the hashtable'''
        # copy the old value of hashtable
        old_table = self.table.copy()
        # make the size equal to next power of 2
        self.size = 2 ** (int(math.log2(self.size)) + 1)
        self.num_items = 0
        self.table = [None for i in range(self.size)]
        # rehash every keys in the existing hashtable
        self.rehash(old_table)

    def rehash(self, oldtable):
        '''Rehashes every keys in the oldtable'''
        for entry in oldtable:
            # for every keys
            if entry is not None and entry is not HashTable.ZOMBIE:
                self.insert(entry.key, entry.value)

    def get(self, key):
        '''Returns the value associated with a key'''
        index = self.find(key)
        if index is None:
            raise RuntimeError('The key does not exist in hash table.')
        else:
            return self.table[index]

    def find(self, key):
        '''Find a particular key inside the hash table and return its index'''
        x = 0
        # keep track of the first zombie we encounter on the track
        first_zombie = -1
        # compute the hash of the key
        h = self.compute_hash(key)

        probed_hash = (h + self.compute_probe(x, key)) % self.size
        # until we reach to the key
        while self.table[probed_hash] is not None:
            if self.table[probed_hash].key == key:
                break
            # keeping track of the first zombie
            if first_zombie < 0 and self.table[probed_hash] == HashTable.ZOMBIE:
                first_zombie = probed_hash
            x = x + 1
            probed_hash = (h + self.compute_probe(x, key)) % self.size

        # now replace the first zombie with the (key, value) we have found
        if self.table[probed_hash] is not None:
            if first_zombie > 0:
                self.table[first_zombie] = self.table[probed_hash]
                self.table[probed_hash] = None
            # return the index for provided key
            return probed_hash
        else:
            return None

    def exists(self, key):
        return self.find(key) is not None

    def remove(self, key):
        '''Remove a key from the hashtable'''
        index = self.find(key)
        if index is None:
            raise RuntimeError('Key does not exist in hashtable.')
        else:
            self.table[index] = HashTable.ZOMBIE
