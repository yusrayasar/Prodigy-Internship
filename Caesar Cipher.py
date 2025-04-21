# open nano editor
nano caesar_cipher.py

# Enter this code
def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')

            if mode == 'encrypt':
                result += chr((ord(char) - offset + shift) % 26 + offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char

    return result


# User input
print("=== Caesar Cipher Tool ===")
message = input("Enter your message: ")
shift = int(input("Enter shift number: "))
mode = input("Choose 'encrypt' or 'decrypt': ")

# Output result
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")

# To run
python3 caesar_cipher.py
