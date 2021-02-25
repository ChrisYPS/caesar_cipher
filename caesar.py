import sys

def caesar(string, shift):
    cipher = ''
    for char in string:
        if((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            if char.isupper():
                cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher = cipher + char
    return cipher

if len(sys.argv) > 1:
    try:
        shift = int(sys.argv[1])
        if shift >= 0:
            text = input("Plaintext: ")
            print("Ciphertext: ", caesar(text, shift))
        else:
            sys.exit("Status Code: 1. Must provide a non negative integer as an argument")
    except:
        sys.exit("Status Code: 1. Must provide a non negative integer as an argument")
else:
    sys.exit("Status Code: 1. Must provide a non negative integer as an argument")
