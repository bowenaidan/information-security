def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    for i, char in enumerate(plain_text):
        index = i % len(key)
        if(char.isupper()):
            encrypted_value = chr(((ord(char) + ord(key[index]) - 130) % 26) + 65)
            encrypted_text = encrypted_text + encrypted_value
        else:
            encrypted_value = chr(((ord(char) + ord(key[index]) - 194) % 26) + 97)
            encrypted_text += encrypted_value
    return encrypted_text

# optimized version (doesn't account for lower case)
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        shift = (ord(char) - ord(key[i % key_length]) + 26) % 26 + 65
        decrypted_text.append(chr(shift))
    return ''.join(decrypted_text)