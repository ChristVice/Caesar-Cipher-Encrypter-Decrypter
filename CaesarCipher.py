import math


def encrypter(text, alphabet, positionShift):
    encryptedText = ""
    for letter in text.lower():
        if letter == " ":
            encryptedText += " "
        else:
            letterIndex = alphabet.index(letter)
            encryptedText += alphabet[(letterIndex+positionShift) % 26] if letterIndex + \
                positionShift > 25 else alphabet[letterIndex+positionShift]
    return encryptedText


def decrypter(text, alphabet, positionShift):
    decryptedText = ""
    for letter in text.lower():
        if letter == " ":
            decryptedText += " "
        else:
            letterIndex = alphabet.index(letter)
            decryptedText += alphabet[(letterIndex-positionShift) % 26] if letterIndex + \
                positionShift > 25 else alphabet[letterIndex-positionShift]
    return decryptedText


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    print("This is the alphabet being used: "+alphabet)

    changeAlpha = input("Do you want a new alphabet? [y/n]")
    if(changeAlpha.lower() == "y"):
        alphabet = input("Enter new alphabet: ")
    else:
        positionShift = int(input("Enter # of shift positions: "))

        decision = input("Do you want to Encrypt? [y/n]")
        if(decision.lower() == "y"):
            encrypt = input("Enter text to encrypt: ")
            print(encrypter(encrypt, alphabet, positionShift))
        else:
            decrypt = input("Enter text to decrypt: ")
            print(decrypter(decrypt, alphabet, positionShift))


if __name__ == "__main__":
    main()
