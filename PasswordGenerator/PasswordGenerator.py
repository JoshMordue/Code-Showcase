import tkinter as tk
import random
import string

window = tk.Tk()
window.title('Password Generator')
window.geometry('500x500')


# def loadVariables():
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#     numbers = string.digits
#     symbols = string.punctuation
#     all_characters = ''


def user_choice():
    if op1 == 1:
        all_characters += lower
    if op2 == 1:
        all_characters += upper
    if op3 == 1:
        all_characters += numbers
    if op4 == 1:
        all_characters += symbols

    gen_password = random.sample(all_characters, passwordlength)
    return gen_password

def loadassets():
    description.pack()
    op1.pack()
    op2.pack()
    op3.pack()
    Descript.pack()
    op4.pack()
    Password_length.pack()
    PassDescript.pack()
    GenPass.pack()
    window.mainloop()


description = tk.Label(window, bg='white', width=50, height='5', text="This application is for generating passwords.\n"
                                                            "Please select from the checkboxes below your preferences")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
all_characters = ''
gen_password = ''


op1 = tk.Checkbutton(window, text='Lower-Case Characters', onvalue=1, offvalue=0)
op2 = tk.Checkbutton(window, text='Upper-Case Characters', onvalue=1, offvalue=0)
op3 = tk.Checkbutton(window, text='Numbers', onvalue=1, offvalue=0)
op4 = tk.Checkbutton(window, text='Symbols', onvalue=1, offvalue=0)
Descript = tk.Label(window, text="Length of the Password")
Password_length = tk.Scale(window, from_=5, to=20, orient='horizontal')
PassDescript = tk.Button(window, text="Generate Password", command=user_choice)

GenPass = tk.Label(window, width=40, height='3')

loadassets()

