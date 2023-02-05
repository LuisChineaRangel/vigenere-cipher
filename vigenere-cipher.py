alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def char_in_alphabet(char):
  if char in alphabet:
    return True
  return False

def encrypt_char(plain_char, key_char):
  if plain_char not in alphabet or key_char not in alphabet:
    return False
  return alphabet[((alphabet.index(plain_char) + alphabet.index(key_char)) % len(alphabet))]

def encrypt(plain_text, key):
  encrypted_text = str()
  for i in range(len(plain_text)):
    if not char_in_alphabet(plain_text[i]):
      return 'Text with invalid characters'
    encrypted_text += encrypt_char(plain_text[i], key[i % len(key)])
  return encrypted_text

def decrypt_char(encripted_char, key_char):
  if encripted_char not in alphabet or key_char not in alphabet:
    return False
  return alphabet[((alphabet.index(encripted_char) - alphabet.index(key_char)) % len(alphabet))]

def decrypt(encrypted_text, key):
  decrypted_text = str()
  for i in range(len(encrypted_text)):
    if not char_in_alphabet(encrypted_text[i]):
      return 'Text with invalid characters'
    decrypted_text += decrypt_char(encrypted_text[i], key[i % len(key)])
  return decrypted_text

while True:
  text = str()
  print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
  print('■          WELCOME TO THE VIGENERE CIPHER TOOL!          ■')
  print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
  print('What would you want to do?')
  print('[1] Encrypt Text.')
  print('[2] Decrypt Text.')
  print('[3] Show Alphabet.')
  print('[0] Exit.')
  print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
  option = input('Option  ->  ')
  print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

  if option not in ['0', '1', '2', '3']:
    print('ERROR. Option Unknown!')
    continue

  if option == '0':
    print('See you soon!')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    break

  if option == '1':
    text = input('Introduce text to encrypt: ')  
  if option == '2':
    text = input('Introduce text to decrypt: ')
  
  if option in ['1', '2']:
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    key = input('Introduce key: ')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    text = text.upper()
    text = text.replace(" ", "")
    key = key.upper()
    key = key.replace(" ", "")

  if option == '1':
    print(encrypt(text, key))
  if option == '2':
    print(decrypt(text, key))
  if option == '3':
    print(alphabet)