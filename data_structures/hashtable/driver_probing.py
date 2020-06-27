from hashtable import HashTableProbing


def calculate_hash(key):
    return key**3 + 7 * key**2 + 3*key + 5


def probe_func_linear(x, k, size):
    return x


def probe_func_quadratic(x, k, size):
    return x**2


def probe_func_double_hashing(x, k, size):
    def second_hash_func(key):
        return key**3
    d = second_hash_func(k) % size
    if d == 0:
        d = 1
    return (d + x) * second_hash_func(k)


def main():
    # hash table resolution by linear probing
    print('Linear Probing')
    htlinear = HashTableProbing(
        8, hash_func=calculate_hash, probe_func=probe_func_linear)
    htlinear.display()
    htlinear.insert(22)
    htlinear.insert(11)
    htlinear.insert(83)
    htlinear.display()
    htlinear.insert(41)
    htlinear.insert(33)
    htlinear.insert(89)
    htlinear.display()
    # removing an item. creates a zombie
    htlinear.remove(33)
    htlinear.display()

    print('\n\nQuadratic Probing')
    htquad = HashTableProbing(
        8, hash_func=calculate_hash, probe_func=probe_func_quadratic, threshold_factor=0.33)
    htquad.display()
    htquad.insert(22)
    htquad.insert(11)
    htquad.insert(83)
    htquad.display()
    htquad.insert(41)
    htquad.insert(33)
    htquad.insert(89)
    # htquad.insert(51)
    htquad.display()

    print('\n\nDouble hashing')
    htdouble = HashTableProbing(
        8, hash_func=calculate_hash, probe_func=probe_func_double_hashing)
    htdouble.display()
    htdouble.insert(22)
    htdouble.insert(11)
    htdouble.insert(83)
    htdouble.display()
    htdouble.insert(41)
    htdouble.insert(33)
    htdouble.insert(89)
    # htdouble.insert(51)
    htdouble.display()


if __name__ == "__main__":
    main()
