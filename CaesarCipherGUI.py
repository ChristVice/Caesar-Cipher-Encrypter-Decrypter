from tkinter import *

root = Tk()
root.title("Caesar Cipher Encrypter/Decrypter")
#root.tk.call('tk', 'scaling', 3.0)

width = 600
height = 320
root.minsize(width, height)
root.maxsize(width, height)

canvas = Canvas(root, width=width, height=height)
canvas.pack()

canvas.create_text(35, 15, text="Alphabet")  # creates the Alphabet label
# creates the entry field below the Alphabet label
alphabetEntry = Entry(root, width=28)
alphabetEntry.insert(0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
canvas.create_window(97, 40, window=alphabetEntry)

canvas.create_text(220, 15, text="Shift")  # creates the Shift label
# creates the entry field below the Shift label
shiftEntry = Entry(root, width=5)
shiftEntry.insert(0, "5")
canvas.create_window(225, 40, window=shiftEntry)

canvas.create_text(35, 70, text="Enter Text")  # creates the Enter Text label
# creates the entry field below the Enter Text label
enterEntry = Text(root, width=28, height=13)
enterEntry.insert(END, "Sample Text")
canvas.create_window(124, 192, window=enterEntry)


# creates the Encryption/Decryption text field
canvas.create_text(430, 70, text="Encrypted/Decrypted Text")
encrypter_decrypter = Text(root, width=28, height=13)
canvas.create_window(475, 192, window=encrypter_decrypter)


def encrypter():
    text = enterEntry.get(1.0, END)
    alphabet = alphabetEntry.get()
    positionShift = int(shiftEntry.get())

    encryptedText = ""  # start blank text
    for letter in text.lower():  # iterate through the text
        if letter == " ":  # if letter is a space, add space to encryptedText
            encryptedText += " "
        elif(alphabet.find(letter) is not -1):  # if the letter is in the alphabet
            # position of the letter in the alphabet
            letterIndex = alphabet.index(letter)
            encryptedText += alphabet[(letterIndex+positionShift) % 26] if letterIndex + \
                positionShift > 25 else alphabet[letterIndex+positionShift]  # if pos+shift > 25, add letter at sum%26 in alpha else add letter at new pos in alpha to encryptedText

    # replaces the text in the field with the encryptedText
    encrypter_decrypter.delete(1.0, END)
    encrypter_decrypter.insert(END, encryptedText)


# create the Encryption button
encryptButton = Button(text='Encrypt ->', command=encrypter)
canvas.create_window(300, 160, window=encryptButton)


def decrypter():
    text = enterEntry.get(1.0, END)
    alphabet = alphabetEntry.get()
    positionShift = int(shiftEntry.get())

    decryptedText = ""  # start blank
    for letter in text.lower():  # iterate through text
        if letter == " ":  # if letter is a space, add space to decryptedText
            decryptedText += " "
        elif(alphabet.find(letter) is not -1):  # if the letter is in the alphabet
            letterIndex = alphabet.index(letter)
            decryptedText += alphabet[(letterIndex-positionShift) % 26] if letterIndex + \
                positionShift > 25 else alphabet[letterIndex-positionShift]  # if the pos-shift > 25, add letter at sum%26 in alpha else add letter at new pos in alpha to decryptedText

    # replaces the text in the field wit the decryptedText
    encrypter_decrypter.delete(1.0, END)
    encrypter_decrypter.insert(END, decryptedText)


# create the Decryption button
decryptButton = Button(text='Decrypt ->', command=decrypter)
canvas.create_window(300, 190, window=decryptButton)


root.mainloop()
