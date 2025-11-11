def main():
    print("Random Number File Reader")
    try:
        with open("randomnum.txt", "r") as file:
            numbers = []
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    numbers.append(int(stripped_line))
            print("List of random numbers in randomnum.txt:")
            for num in numbers:
                print(num)
            print(f"Random number count: {len(numbers)}")
    except FileNotFoundError:
        print("Error: The file 'randomnum.txt' was not found.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()