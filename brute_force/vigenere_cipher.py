def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    for i, char in enumerate(plain_text):
        index = i % len(key)
        if(char.isupper()):
            encrypted_value = chr(((ord(char) + ord(key[index]) - 65 - 65) % 26) + 65)
            encrypted_text = encrypted_text + encrypted_value
        else:
            encrypted_value = chr(((ord(char) + ord(key[index]) - 97 - 97) % 26) + 97)
            encrypted_text += encrypted_value
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    for i, char in enumerate(encrypted_text):
        index = i % len(key)
        if(char.isupper()):
            decrypted_value = chr(((ord(char) - ord(key[index]) + 26) % 26) + 65)
            decrypted_text = decrypted_text + decrypted_value
        else:
            decrypted_value = chr(((ord(char) - ord(key[index]) + 26) % 26) + 97)
            decrypted_text += decrypted_value
    return decrypted_text

plain_text = "JAYHAWK"
key = "EECS"
encrypted_text = vigenere_encrypt(plain_text, key)
print(encrypted_text)
print(vigenere_decrypt(encrypted_text, key))
