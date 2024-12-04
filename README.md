# PRODIGY_CS_01

### Caesar Cipher Program

---

#### Overview
This Caesar Cipher program is a Python-based tool that implements the classic Caesar Cipher encryption technique. It allows users to encrypt and decrypt messages by shifting each letter of the alphabet by a specified number of positions. The program is designed to handle both uppercase and lowercase letters, while leaving non-alphabetic characters unchanged.

---

#### Features
- **Encryption and Decryption**: Provides functionality to encrypt and decrypt messages using the Caesar Cipher method.
- **Case Handling**: Supports both uppercase and lowercase letters, ensuring the case is preserved.
- **Non-Alphabetic Characters**: Non-alphabetic characters, such as spaces and punctuation, are not altered.
- **Interactive Interface**: A simple command-line interface that guides users through the encryption and decryption processes.

---

#### Requirements
- Python 3.x (any version).

---

#### How to Use the Program

1. **Run the Program**:
   ```bash
   python caesar_cipher.py
   ```

2. **Choose an Operation**:
   - Type `encrypt` to encode a message.
   - Type `decrypt` to decode a message.
   - Type `exit` to quit the program.

3. **Provide the Inputs**:
   - Enter the message you want to process.
   - Specify the shift value (positive integer).

4. **Output**:
   - The encrypted or decrypted message will be displayed.

---

#### Example Usage

**Encrypting a Message:**
```
Would you like to 'encrypt' or 'decrypt' a message? (Type 'exit' to quit): encrypt
Enter the message: Hello, World!
Enter the shift value (a positive integer): 3

The encrypted message is: Khoor, Zruog!
```

**Decrypting a Message:**
```
Would you like to 'encrypt' or 'decrypt' a message? (Type 'exit' to quit): decrypt
Enter the message: Khoor, Zruog!
Enter the shift value (a positive integer): 3

The decrypted message is: Hello, World!
```
![TASK 1](https://github.com/user-attachments/assets/c7d77403-3170-4ee3-a8b3-4d9f3754915a)

---

#### Code Insights
The program works by shifting each alphabetical character in the input string according to the specified shift value. It uses modular arithmetic to ensure the shift wraps around when it reaches the end of the alphabet. Non-alphabetic characters are appended to the result without modification.

---

#### Future Enhancements
Plans include:
- Supporting additional symbols or characters.
- Adding a graphical interface for easier interaction.
- Exploring more advanced cryptographic algorithms.

---

#### License
This project is free to use and modify for educational purposes or personal projects.

---

Thank you for using the program!
