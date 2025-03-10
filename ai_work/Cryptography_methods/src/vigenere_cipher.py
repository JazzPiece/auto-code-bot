def vigenere_cipher(text, keyword):
    result = ""
    keyword = keyword.upper()
    key_length = len(keyword)
    for i, char in enumerate(text):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift = ord(keyword[i % key_length]) - 65
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

text = "Hello, World!"
keyword = "KEY"
encrypted_text = vigenere_cipher(text, keyword)
print("Encrypted text:", encrypted_text)