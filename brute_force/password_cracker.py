from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

def password_crack(ciphertext, keyLength, firstWorldLength):
    for i in range(65, 91):
        for j in range(65, 91):
            print(chr(i) + chr(j))

password_crack("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6)