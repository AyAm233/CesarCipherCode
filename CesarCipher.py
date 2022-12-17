def encrypt(text,key):
    Decrypted_text = ""

    for i in range(len(text)):
        char = text[i]


        if(char.isupper()):

            Decrypted_text += chr((ord(char) + key - 65) % 26 + 65)

        else:
            Decrypted_text += chr((ord(char) + key - 97) % 26 + 97)

    return Decrypted_text

def Decrypt(text,key):
    encrypted_text = ""

    for i in range(len(text)):
        char = text[i]


        if(char.isupper()):

            encrypted_text+=chr((ord(char) - key - 65) % 26 + 65)

        else:
            encrypted_text+=chr((ord(char) - key - 97) % 26 + 97)

    return encrypted_text

while 1:

    print('Press 1 for Encryption \n Press 2 for Decryption \n Press 0 to exit.. ')

    choice = input('Insert choice : ')
    if choice.isdigit():
        if choice == '1':
            text = input('Insert the plaintext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print('------------------------------------------------------------------------------')
            print("Cipher: " + encrypt(text, key))  
            con = input('continue ? [Any Key/n]')
            if con == 'n':
                print('Exit')
                break
            else:
                pass
        elif choice == '2':
            text = input('Insert the ciphertext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print('------------------------------------------------------------------------------')
            print("plain: " + Decrypt(text, key))  
            con = input('continue ? [Any Key/n]')
            if con == 'n':
                print('Exit')
                break
            else:
                pass

        elif choice == '0':
            print('Exit')
            break
        else:
            print('error .. \n'
                  'Please insert 1 or 2 ')



