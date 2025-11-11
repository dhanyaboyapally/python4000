import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Random Number File Writer")
    quantity = get_positive_integer("How many random numbers do you want? ")
    lower = get_positive_integer("What is the lowest the random number should be? ")
    while True:
        upper = get_positive_integer("What is the highest the random number should be? ")
        if upper >= lower:
            break
        print("Upper bound must be greater than or equal to lower bound.")
    try:
        with open("randomnum.txt", "w") as file:
            for _ in range(quantity):
                num = random.randint(lower, upper)
                file.write(f"{num}\n")
        print("The random numbers were written to randomnum.txt")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()