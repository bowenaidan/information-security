import time
from vigenere_cipher import vigenere_decrypt

word_dict = set()
with open("dict.txt", "r") as dictionary:
    for line in dictionary:
        entry = line.strip()
        word_dict.add(entry)
        

def keyGen(keyLength, prefix=''):
    if keyLength == 0:
        yield prefix
    else:
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for combo in keyGen(keyLength - 1, prefix + letter):
                yield combo


def password_crack(ciphertext, keyLength, firstWordLength):
    possible_translations = []
    for key in keyGen(keyLength):
        decrypted = vigenere_decrypt(ciphertext[:firstWordLength], key)
        if decrypted in word_dict:
            possible_translations.append(vigenere_decrypt(ciphertext, key))
            print(key)
            return possible_translations


        
print("1. ")
start_time = time.time()
print(password_crack("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6))
print("--- %s seconds ---" % round((time.time() - start_time), 5))

print("2. ")
start_time = time.time()
print(password_crack("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7))
print("--- %s seconds ---" % round((time.time() - start_time), 5))

print("3. ")
start_time = time.time()
print(password_crack("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10))
print("--- %s seconds ---" % round((time.time() - start_time), 5))

print("4. ")
start_time = time.time()
print(password_crack("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11))
print("--- %s seconds ---" % round((time.time() - start_time), 5))

print("5. ")
start_time = time.time()
print(password_crack("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9))
print("--- %s seconds ---" % round((time.time() - start_time), 5))

print("6. ")
start_time = time.time()
print(password_crack("VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO", 7, 13))
print("--- %s seconds ---" % round((time.time() - start_time), 5))


# Output:

# 1. 
# KS
# ['CAESARSWIFEMUSTBEABOVESUSPICION']
# --- 0.00126 seconds ---
# 2. 
# KEY
# ['FORTUNEWHICHHASAGREATDEALOFPOWERINOTHERMATTERSBUTESPECIALLYINWARCANBRINGABOUTGREATCHANGESINASITUATIONTHROUGHVERYSLIGHTFORCES']
# --- 0.02685 seconds ---
# 3. 
# IWKD
# ['EXPERIENCEISTHETEACHEROFALLTHINGS']
# --- 0.79653 seconds ---
# 4. 
# KELCE
# ['IMAGINATIONISMOREIMPORTANTTHANKNOWLEDGE']
# --- 24.46698 seconds ---
# 5. 
# HACKER
# ['EDUCATIONISWHATREMAINSAFTERONEHASFORGOTTENWHATONEHASLEARNEDINSCHOOL']
# --- 384.11028 seconds ---
# 6. 
# NICHOLS
# ['INTELLECTUALSSOLVEPROBLEMSGENIUSESPREVENTTHEM']
# --- 23691.53613 seconds ---
