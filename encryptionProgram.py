#!/usr/bin/python

from tkinter import *
from tkinter import messagebox
from encryptMessage import encryptMessage, decryptMessage

message = ''
sec_mess = ''
sec_mess_decr = ''

def get_message():
    global mess
    global sec_mess
    global message
    message = mess.get()
    enc = encryptMessage(message)
    cod = enc.make_key_code()
    sec_mess = enc.encrypt_message(cod)
    print(sec_mess)

def get_message_decrypt():
    global mess_decr
    global sec_mess_decr
    mess_decr = mess_decr.get()
    enc = encryptMessage('X')
    cod = enc.make_key_code()
    dec = decryptMessage()
    dec_fin = dec.decipher(mess_decr, cod)
    print(dec_fin)

root = Tk()

var = StringVar()
var.set("Enter your message to be encrypted here:")
l1 = Label(root, textvariable=var, relief=RAISED)
l1.grid(column=1, row=1)


mess = Entry(root, bd=5)
mess.grid(column=2, row=1)

but1 = Button(root, text="Submit Message:", command=get_message)
but1.grid(column=1, row=3)

var2 = StringVar()
var2.set("Enter your message to be decrypted here:")
l2 = Label(root, textvariable=var2, relief=RAISED)
l2.grid(column=1, row=2)

mess_decr = Entry(root, bd=5)
mess_decr.grid(column=2, row=2)


but2 = Button(root, text='Submit Message For Decryption:', command=get_message_decrypt)
but2.grid(column=3, row=3)

root.mainloop()
