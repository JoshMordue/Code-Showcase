import tkinter as tk
import random
import string

window = tk.Tk()
window.title('Password Generator')
window.geometry('500x500')


def generator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    all_characters = ''

    option1 = op1.getvar()
    option2 = op2.getvar()
    option3 = op3.getvar()
    option4 = op4.getvar()
    password_length = Pass_length.get()
    count = 0

    print(option1)
    print(op1)
    print(lower)
    if option1.get():
        print(lower)
        all_characters += lower
        count += 1
    if option2 == 1:
        all_characters += upper
        count += 1
    if option3 == 1:
        all_characters += numbers
        count += 1
    if option4 == 1:
        all_characters +=
        count += 1

    for i in range(password_length):
        for x in range(x)
            password_length -= 1
            if
        for y in range(y)


    GenPass.insert(0, all_characters)
    print(all_characters)


def build():
    description.pack()
    op1.pack()
    op2.pack()
    op3.pack()
    op4.pack()
    Descript.pack()
    Pass_length.pack()
    PassDescript.pack()
    GenPass.pack()
    window.mainloop()


description = tk.Label(window, bg='white', width=50, height='5', text="This application is for generating passwords.\n"
                                                            "Please select from the checkboxes below your preferences")


op1 = tk.Checkbutton(window, text='Lower-Case Characters', onvalue=1, offvalue=0)
op2 = tk.Checkbutton(window, text='Upper-Case Characters', onvalue=1, offvalue=0)
op3 = tk.Checkbutton(window, text='Numbers', onvalue=1, offvalue=0)
op4 = tk.Checkbutton(window, text='Symbols', onvalue=1, offvalue=0)
Descript = tk.Label(window, text="Length of the Password")
Pass_length = tk.Scale(window, from_=5, to=20, orient='horizontal')
PassDescript = tk.Button(window, text="Generate Password", command=generator)
GenPass = tk.Entry(window, width=40)

build()

