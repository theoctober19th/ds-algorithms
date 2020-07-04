from data_structures.doubly_linked_list import DoublyLinkedList

# creating a doubly linked list
animals = DoublyLinkedList()

print('Adding a few elements on the front...')
animals.insert_front('Cow')
animals.insert_front('Tiger')
animals.display()

print('\nAdding a few elements on the back...')
animals.insert_back('Lion')
animals.insert_back('Wolf')
animals.display()

print('\nAdding an item after Lion')
animals.insert_after('Lion', 'Lioness')
animals.display()

print('\nRemoving a few items from beginning..')
animals.remove_front()
animals.remove_front()
animals.display()

print('\nRemoving Lioness from the list')
animals.remove('Lioness')
animals.display()

print('\nRemoving a few items from the back')
animals.remove_back()
animals.remove_back()
animals.display()

print('\nThere are {} items on the list.'.format(animals.size))
