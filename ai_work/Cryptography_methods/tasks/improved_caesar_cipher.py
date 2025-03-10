def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt_caesar_cipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
print("Decrypted text:", decrypted_text)