import tkinter 
from tkinter import *
import random

root = Tk()
root.title("Password Generator 2.0")
root.geometry("700x400")
root.config(background="cadetblue1")

def Generate_passward(self):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    length = Length.getint(s=0)
    password = ""
    for a in range(length):
        password+=random.choice(chars)

    right=str(password)
    cs = Label(root, text="The Generated Password is :", font=("poppins", 20), bg="cadetblue1", fg="#364971")
    cs.place(x=200, y=300)
    spell1=spell
    spell1.config(text=right)
    


heading = Label(root, text="Password Generator 2.0", font=("Trebuchet MS", 30, "bold"),bg="cadetblue1", fg="#364971")
heading.pack(pady=(50,0))

Length = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
Length.pack(pady=10)
Length.focus()

heading2 = Label(root, text="Click to Generate...", font=("Trebuchet MS", 20),bg="cadetblue1", fg="#364971")
heading2.pack(pady=10)

Button=Button(root, text="Generate", font=("arial", 20, "bold"), fg="white", bg="red", command=Generate_passward)
Button.pack()

spell=Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)
spell= Generate_passward()



root.mainloop()
