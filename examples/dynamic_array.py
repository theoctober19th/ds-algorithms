# creating a new dynamic array with some elements (List in Python)
darray = [1, 5, 8]

print(darray)
print('Length of the array:', len(darray))

print('\nAdding an item to the end of this array')
darray.append(12)
print(darray)

print('\nInserting an item at index 1')
darray.insert(1, 44)
print(darray)

print('\nRemoving an item at index 1')
darray.pop(1)
print(darray)

print('\nRemoving the value 8 from array')
darray.remove(8)
print(darray)
