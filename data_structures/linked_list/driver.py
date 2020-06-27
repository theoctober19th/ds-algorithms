from data_structures.linked_list.linked_list import LinkedList


def main():
    animals = LinkedList()
    animals.insert_last("Dog")
    animals.insert_last("Cat")
    animals.insert_last("Horse")
    animals.insert_after("Dog", "Giraffe")
    animals.insert_first("Apple")
    animals.display()

    animals.remove("Apple")
    animals.display()
    print("List contains {} elements.".format(animals.size()))


if __name__ == "__main__":
    main()
