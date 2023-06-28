import tkinter as tk
import random
import string
import pyperclip


def generator():
    """assigns variables for the character types, clears the field (in the case of a user requiring another password.
    depending on user choice on password strength, select a sample of random characters using upper,lower, numbers
    and special characters. Send the randomised password to the GenPass field"""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    GenPass.delete(0, 'end')

    all_characters = lowercase+uppercase+numbers+symbols
    password_length = Pass_length.get()

    if choice.get() == 1:
        GenPass.insert(0, random.sample(lowercase + uppercase, password_length))

    elif choice.get() == 2:
        GenPass.insert(0, random.sample(lowercase + uppercase + numbers, password_length))

    elif choice.get() == 3:
        GenPass.insert(0, random.sample(all_characters, password_length))


def copy():
    """copies the randomised password when generated to the users clipboard"""
    random_password = GenPass.get()
    random_password = random_password.replace(" ", "")
    pyperclip.copy(random_password)


def build():
    """handles all the .pack functions"""
    description.pack()
    weak_radioButton.pack()
    medium_radioButton.pack()
    strong_radioButton.pack()
    Descript.pack()
    Pass_length.pack()
    PassDescript.pack()
    GenPass.pack()
    Copy_button.pack()
    window.mainloop()


window = tk.Tk()
window.title('Password Generator')
window.geometry('500x500')

choice = tk.IntVar()

description = tk.Label(window, bg='white', width=50, height='5', text="PASSWORD GENERATOR\n"
                                                            "Please select from the options below your password \n"
                                                                      "strength preference")


weak_radioButton = tk.Radiobutton(window, text='Weak', value=1, variable=choice)
choice.set(1)
medium_radioButton = tk.Radiobutton(window, text='Medium', value=2, variable=choice)
strong_radioButton = tk.Radiobutton(window, text='Strong', value=3, variable=choice)
Descript = tk.Label(window, text="Length of the Password")
Pass_length = tk.Scale(window, from_=7, to=20, orient='horizontal')
PassDescript = tk.Button(window, text="Generate Password", command=generator)
GenPass = tk.Entry(window, width=40)
Copy_button = tk.Button(window, text="Copy Password", command=copy)

build()
