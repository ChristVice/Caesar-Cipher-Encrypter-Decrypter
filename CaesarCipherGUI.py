from tkinter import *

root = Tk()

root.geometry("500x200")

mainLabel = Label(
    root, text="Enter text to encrypt/decrypt").grid(row=0, sticky=W)

text = Entry(root)

text.grid(row=1, sticky=W)


root.mainloop()
