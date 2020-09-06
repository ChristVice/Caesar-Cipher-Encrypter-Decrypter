from tkinter import *


textBoxHeight = 10
textBoxWidth = 30

root = Tk()
root.title("Caesar Cipher Encrypter/Decrypter")
root.tk.call('tk', 'scaling', 3.0)

'''
root.minsize(700, 200)
root.maxsize(700, 200)
'''

# All the frames being used LEFT,MIDDLE,RIGHT
leftFrame = Frame(root, bd=6)  # , bg="green")
leftFrame.pack(side=LEFT)
middleFrame = Frame(leftFrame)  # ,  bg="gray")
middleFrame.pack(side=RIGHT)
rightFrame = Frame(middleFrame)  # , bg="red")
rightFrame.pack(side=RIGHT)

plainTitle = Label(leftFrame, text="Plaintext/Decrypted Text")
plainTextString = Text(leftFrame, height=textBoxHeight, width=textBoxWidth)
plainTitle.pack()
plainTextString.pack(side=BOTTOM)

#button = Button(middleFrame, text="Encrypt/Decrypt")
buttonTitle = Label(middleFrame, text="Encrypt", width=15)
buttonTitle.pack()

encryptTitle = Label(rightFrame, text="Encrypted Text")
encryptTextString = Text(rightFrame, height=textBoxHeight, width=textBoxWidth)
encryptTitle.pack()
encryptTextString.pack(side=BOTTOM)

# if(not plainTextString or not encryptTextString):
# while(True):
buttonTitle['text'] = "something"


root.mainloop()
