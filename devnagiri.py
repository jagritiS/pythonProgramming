from random import shuffle
from string import printable
import tkinter as tk
import random

chars=["क","ख","ग","घ","ङ","च","छ","ज","झ","ण","त","थ","द","ध","न","प","फ","ब","भ",
"म","य","र","ल","व","स","श","ष","ह","ञ","ै","ौ","ृ","ु","ू","ि","ी","ो","ा","े",'0', 
'1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
keys=list(chars)
shuffled_keys=list(chars)
shuffle(shuffled_keys) 
maps=dict(zip(keys,shuffled_keys))
reversed_maps=dict(zip(shuffled_keys,keys)) 
def d_encrypt(message):
    cipher=[]    
    for c in message:
          if c in chars:
            cipher.append(maps[c])
          else:
            cipher.append(c)
    return"".join(cipher) 
def d_decrypt(cipher):
    plain_text = []
    for c in cipher:
        if c in chars:
            plain_text.append(reversed_maps[c])
        else:
            plain_text.append(c)
    return''.join(plain_text)


master = tk.Tk()
master.title("Devnagiri and English Alphabet Text Encryption")
master.geometry('800x300')
master.configure(background = "teal");

def Take_input():
   inputs =  e1.get()
   e2.insert(10, d_encrypt(inputs))
def Decrypt_input():
    inputs =  e1.get()
    e3.insert(10, d_decrypt(d_encrypt(inputs)))
def Clear_input(): 	    
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0,tk.END)

tk.Label(master, 
         text="Plain Text",bg="teal").place(x = 20,y = 10)
tk.Label(master, 
         text="Encrypted Text",bg="teal").place(x = 250,y = 10)
tk.Label(master, 
         text="Decrypted Text",bg="teal").place(x = 500,y = 10)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e1.place(x = 20,y = 30,width=200,height=100)
e2.place(x = 250,y = 30,width=200,height=100)
e3.place(x = 500,y = 30,width=200,height=100)

btn1 = tk.Button(master,text='Clear',command=Clear_input)
btn1.place(x = 150,y = 150)
btn2 = tk.Button(master,text='Encrypt', command=Take_input)
btn2.place(x = 30,y = 150)
btn3 = tk.Button(master,text='Decrypt', command=Decrypt_input)
btn3.place(x = 250,y = 150)

tk.mainloop()
