from hashtable import HashTableChaining


def calculate_hash(key):
    return key**3 + 7 * key**2 + 3*key + 5


def main():
    # hash table resolution by chaining
    hashtable = HashTableChaining(5, hash_func=calculate_hash)
    print('Inserting a bunch of elements into the hashtable.')
    hashtable.insert(76)
    hashtable.insert(12)
    hashtable.insert(29)
    hashtable.insert(11)
    hashtable.insert(23)
    hashtable.display()

    print('The size of hashtable is now about to be doubled')
    # each key gets rehashed again
    hashtable.insert(55)
    hashtable.display()

    print('Searching for a key')
    print(hashtable.contains(12))
    print(hashtable.find(12))

    print('\nRemoving a key')
    hashtable.remove(55)
    hashtable.display()


if __name__ == "__main__":
    main()
