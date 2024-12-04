def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            
            # Apply shift and wrap around using modulo
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += new_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

# Main program loop
def main():
    print("Caesar Cipher Program")
    while True:
        mode = input("\nWould you like to 'encrypt' or 'decrypt' a message? (Type 'exit' to quit): ").lower()
        
        if mode == 'exit':
            print("Goodbye!")
            break
        elif mode not in ['encrypt', 'decrypt']:
            print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (a positive integer): "))
        
        result = caesar_cipher(message, shift, mode)
        print(f"\nThe {mode}ed message is: {result}")

if __name__ == "__main__":
    main()
