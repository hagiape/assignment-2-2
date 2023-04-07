# create decyphering program
# vowel lists
english_vowels = ['a', 'e', 'i', 'o', 'u']
encrypted_vowels = ['*', '&', '#', '+', '!']

# ask input from user
encrypted_text = input('Enter a string to decrypt: ')
# placeholder variable
decrypted_text = 'The plain text: ' + '\033[33m' 

# main code
for i in range(len(encrypted_text)):
    if encrypted_text[i] in encrypted_vowels:
        list_index = encrypted_vowels.index(encrypted_text[i])
        decrypted_text += english_vowels[list_index]
    else:
        decrypted_text += encrypted_text[i]

print('\033[32m~' * (len(decrypted_text) - 5) + '\033[0m')
print(decrypted_text + '\033[0m')
print('\033[32m~' * (len(decrypted_text) - 5) + '\033[0m')