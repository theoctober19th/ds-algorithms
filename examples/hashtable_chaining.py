from data_structures.hashtable.chaining import HashTable


def calculate_hash(key):
    return key**3 + 7 * key**2 + 3*key + 5


def main():
    print('Creating new hash table')
    htlinear = HashTable(
        8, hash_func=calculate_hash)
    htlinear.display()

    print('\nInserting some values...')
    htlinear.insert(22, 'qwve')
    htlinear.insert(11, 'sdf')
    htlinear.insert(83, 'qwere')
    htlinear.display()

    print('\nInserting some more values')
    htlinear.insert(41, 'vnn')
    htlinear.insert(33, 'pohv')
    htlinear.insert(89, 'braxe')
    htlinear.display()

    print('\nRemoving an item...')
    htlinear.remove(33)
    htlinear.display()


if __name__ == "__main__":
    main()
