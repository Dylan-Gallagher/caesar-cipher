letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mode = input("Do you want to encrypt (e) or decrypt (d): ")


def encrypt(text, usr_key):
    plaintext_list = list(text)
    returned_string = ""
    for char in plaintext_list:
        if char.isalpha():
            index = letters.index(char)
            index += key
            if index >= 52:
                index -= 52
            returned_string += letters[index]
        else: # not letters
            returned_string += char
    return returned_string


def decrypt(text, usr_key):
    ciphertext_list = list(text)
    returned_string = ""
    for char in ciphertext_list:
        if char.isalpha():
            index = letters.index(char)
            index -= key
            if index >= 52:
                index += 52
            returned_string += letters[index]
        else:  # not letters
            returned_string += char
    return returned_string


while True:
    # Encrypt Mode
    if mode == "e":
        plaintext = input("Enter the text you want encrypted\n")
        key = input("Enter the key you want to use (1-52)\n")
        try:
            key = int(key)
        except:
            print("Please enter a number between 1-52 for a key")
            break
        ciphertext = encrypt(plaintext, key)
        print("Your encrypted text is: \n" + ciphertext)
        break
    # Decrypt Mode
    elif mode == "d":
        ciphertext = input("Enter the text you want decrypted\n")
        key = input("Enter the key you want to use (1-52)\n")
        try:
            key = int(key)
        except:
            print("Please enter a number between 1-52 for a key")
            break
        plaintext = decrypt(ciphertext, key)
        print("Your decrypted text is: \n" + plaintext)
        break
    # Error handling
    else:
        print("Please enter either 'd' or 'e'")
        break
