from data_structures.linked_list.linked_list import LinkedList
from data_structures.linked_list.linked_list import Node
import math
# python has builtin dictionary data type
# which is an optimized implementation of hashtable
# but i have tried to implement hashtable from scratch
# just so we know how it works


class HashTableChaining:
    def __init__(self, size, hash_func, threshold_factor=0.8):
        self.size = size
        self.num_items = 0
        self.filled_buckets = 0
        self.table = [LinkedList() for i in range(size)]
        self.hash_func = hash_func
        self.threshold_factor = threshold_factor

    def compute_hash(self, key):
        return self.hash_func(key) % self.size

    def insert(self, key, payload=None):
        i = self.compute_hash(key)
        bucket = self.table[i]
        if bucket.head == None:
            self.filled_buckets = self.filled_buckets + 1
        bucket.insert_last(key, payload)
        self.num_items = self.num_items + 1
        if self.filled_buckets > self.size * self.threshold_factor:
            self.resize()

    def resize(self):
        oldtable = self.table.copy()
        self.size = self.size * 2
        self.table = [LinkedList() for i in range(self.size)]
        self.num_items = 0
        self.filled_buckets = 0
        self.rehash(oldtable)

    def rehash(self, oldtable):
        for bucket in oldtable:
            trav = bucket.head
            while trav is not None:
                self.insert(trav.key, trav.payload)
                trav = trav.next

    def display(self):
        for index, bucket in enumerate(self.table):
            print('Bucket', index, end=': ')
            bucket.display()
        print()

    def find(self, key):
        index = self.compute_hash(key)
        bucket = self.table[index]
        trav = bucket.head
        while trav != None:
            if trav.key == key:
                return trav
            trav = trav.next
        return None

    def contains(self, key):
        return True if self.find(key) is not None else False

    def remove(self, key):
        index = self.compute_hash(key)
        bucket = self.table[index]
        bucket.remove(key)

    def get(self, key):
        node = find(key)
        if node is None:
            raise RuntimeError('Key does not exist.')
        else:
            return node


class HashTableProbing:
    ZOMBIE = Node()

    def __init__(self, size, hash_func, probe_func, threshold_factor=0.66):
        self.size = size
        self.num_items = 0
        self.table = [None for i in range(size)]
        self.hash_func = hash_func
        self.probe_func = probe_func
        self.threshold_factor = threshold_factor

    def compute_hash(self, key):
        return self.hash_func(key) % self.size

    def compute_probe(self, probe, key):
        return self.probe_func(probe, key, self.size)

    def display(self):
        for item in self.table:
            if item is None:
                print(item, end=' ')
            elif item is HashTableProbing.ZOMBIE:
                print('ZOMBIE', end=' ')
            else:
                print(item.key, end=' ')
        print()

    def insert(self, key, payload=None):
        x = 0
        h = self.compute_hash(key)
        probed_hash = (h + self.compute_probe(x, key)) % self.size
        while self.table[probed_hash] is not None and self.table[probed_hash] != HashTableProbing.ZOMBIE:
            x = x + 1
            probed_hash = (h + self.compute_probe(x, key)) % self.size
        self.table[probed_hash] = Node(key, payload)
        self.num_items = self.num_items + 1
        if self.num_items > self.threshold_factor * self.size:
            self.resize()

    def resize(self):
        old_table = self.table.copy()
        self.size = 2 ** (int(math.log2(self.size)) + 1)
        self.num_items = 0
        self.table = [None for i in range(self.size)]
        self.rehash(old_table)

    def rehash(self, oldtable):
        for item in oldtable:
            if item is not None and item is not HashTableProbing.ZOMBIE:
                self.insert(item.key, item.payload)

    def find(self, key):
        x = 0
        first_zombie = -1
        h = self.compute_hash(key)
        probed_hash = (h + self.compute_probe(x, key)) % self.size
        while self.table[probed_hash] is not None:
            if self.table[probed_hash].key == key:
                break
            if first_zombie < 0 and self.table[probed_hash] == HashTableProbing.ZOMBIE:
                first_zombie = probed_hash
            x = x + 1
            probed_hash = (h + self.compute_probe(x, key)) % self.size
        if first_zombie > 0 and self.table[probed_hash] is not None:
            self.table[first_zombie] = self.table[probed_hash]
            self.table[probed_hash] = None
        return self.table[probed_hash]

    def contains(self, key):
        return True if self.find(key) is not None else False

    def remove(self, key):
        if self.find(key) is None:
            raise RuntimeError('Key does not exist in hashtable.')
        else:
            x = 0
            h = self.compute_hash(key)
            probed_hash = (h + self.compute_probe(x, key)) % self.size
            while self.table[probed_hash] is not None:
                if self.table[probed_hash].key == key:
                    self.table[probed_hash] = HashTableProbing.ZOMBIE
                    break
                x = x + 1
                probed_hash = (h + self.compute_probe(x, key)) % self.size
