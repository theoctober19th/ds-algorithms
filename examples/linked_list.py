from data_structures.linked_list import LinkedList


def main():
    animals = LinkedList()
    animals.insert_back("Dog")
    animals.insert_back("Cat")
    animals.insert_front("Horse")
    animals.insert_after("Dog", "Giraffe")
    animals.insert_front("Apple")
    animals.display()

    animals.remove("Apple")
    animals.display()
    print("List contains {} elements.".format(animals.size))


if __name__ == "__main__":
    main()
