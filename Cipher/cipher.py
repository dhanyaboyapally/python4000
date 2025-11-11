# Cipher dictionary for encoding and decoding
CIPHER_RULES = {
    'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6',
    'h': '7', 'i': '8', 'j': '9', 'k': '!', 'l': '@', 'm': '#', 'n': '$',
    'o': '%', 'p': '^', 'q': '&', 'r': '*', 's': '(', 't': ')', 'u': '-',
    'v': '+', 'w': '<', 'x': '>', 'y': '?', 'z': '='
}

# Reverse cipher dictionary for decoding
REVERSE_CIPHER_RULES = {value: key for key, value in CIPHER_RULES.items()}

def encode_message(message):
    """Encodes the given message using the cipher rules."""
    encoded = ""
    for char in message:
        if char in CIPHER_RULES:  # Encode only if character is in cipher
            encoded += CIPHER_RULES[char]
        else:
            encoded += char  # Pass through unchanged for unsupported characters
    return encoded

def decode_message(message):
    """Decodes the given message using the cipher rules."""
    decoded = ""
    for char in message:
        if char in REVERSE_CIPHER_RULES:  # Decode only if character is in reverse cipher
            decoded += REVERSE_CIPHER_RULES[char]
        else:
            decoded += char  # Pass through unchanged for unsupported characters
    return decoded

def display_menu():
    """Displays the main menu and returns the user's choice."""
    print("\nWelcome to the Secret Message Encoder/Decoder")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")
    while True:
        choice = input("\nWhat would you like to do? ")
        if choice in {'1', '2', '3'}:
            return choice
        print("Invalid choice. Please enter a number between 1 and 3.")

def main():
    """Main function to run the Cipher program."""
    while True:
        choice = display_menu()
        if choice == '1':  # Encode a message
            message = input("\nEnter a message to encode: ").lower()
            encoded_message = encode_message(message)
            print(f"Encoded message: {encoded_message}")
        elif choice == '2':  # Decode a message
            message = input("\nEnter a message to decode: ")
            decoded_message = decode_message(message)
            print(f"Decoded message: {decoded_message}")
        elif choice == '3':  # Exit
            # print("Goodbye!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()
