from Animal import Animal

def main():
    animals = []
    print("Welcome to the animal generator!")
    print("This program creates Animal objects.")

    while True:
        animal_type = input("What type of animal would you like to create? ")
        name = input("What is the animal’s name? ")
        animal = Animal(animal_type, name)
        animals.append(animal)

        repeat = input("Would you like to add more animals (y/n)? ").lower()
        if repeat != 'y':
            break

    print("\nAnimal List:")
    for animal in animals:
        print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")

if __name__ == "__main__":
    main()