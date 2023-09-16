from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

def keyGen(keyLength, prefix=''):
    if keyLength == 0:
        yield prefix
    else:
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for combo in keyGen(keyLength - 1, prefix + letter):
                yield combo


def password_crack(ciphertext, keyLength, firstWorldLength):
    combinations = keyGen(keyLength, "")
    for combination in combinations:
        print(combination)
        

ciphertext = "FEJKLVENAIHOVLEFJE"
firstWorldLength = 5

password_crack(ciphertext, 4, firstWorldLength)
# password_crack("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6)