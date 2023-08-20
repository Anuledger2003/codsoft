from tkinter import *
import string
import random


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(all,password_length))


root=Tk()
root.config(bg='#eb345e')
choice=IntVar()
Font=(' DejaVu Sans Mono',17,'bold')
passwordLabel=Label(root,text='Password Generator',font=(' DejaVu Sans Mono',20,'bold'),fg='black')
passwordLabel.grid(pady=20)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=10)

strongradioButton=Radiobutton(root,text='Strong',value=2,variable=choice,font=Font)
strongradioButton.grid(pady=10)

lengthLabel=Label(root,text='Password Length',font=Font,fg='#1f0d4a')
lengthLabel.grid(pady=15)

length_Box=Spinbox(root,from_=5,to_=18,width=8,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=10)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()


root.mainloop()
