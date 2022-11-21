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

    op1.se
    option_array = op1+op2+op3+op4
    print(option_array)

    password_length = Pass_length.get()
    count = 0

    # for i in range(4):
    #     print(option_array)
    #     print(i)
    #     if option_array[i] == '0':
    #         count+= 1
def build():
    Pass_length
    Descript.pack()
    Pass_length.pack()
    PassDescript.pack()
    GenPass.pack()



description = tk.Label(window, bg='white', width=50, height='5', text="This application is for generating passwords.\n"
                                                            "Please select from the checkboxes below your preferences")
buttonDic = {
    'op1': 0,
    'op2': 0,
    'op3': 0,
    'op4': 0,
}

for key in buttonDic:
    buttonDic[key] = tk.IntVar()
    aCheckButton = tk.Checkbutton(text=key,
                                  variable=buttonDic[key])
    aCheckButton.grid(sticky='w')



# op1 = tk.Checkbutton(window, text='Lower-Case Characters', onvalue=1, offvalue=0)
# op2 = tk.Checkbutton(window, text='Upper-Case Characters', onvalue=1, offvalue=0)
# op3 = tk.Checkbutton(window, text='Numbers', onvalue=1, offvalue=0)
# op4 = tk.Checkbutton(window, text='Symbols', onvalue=1, offvalue=0)
Descript = tk.Label(window, text="Length of the Password")
Pass_length = tk.Scale(window, from_=5, to=20, orient='horizontal')
PassDescript = tk.Button(window, text="Generate Password", command=generator)
GenPass = tk.Entry(window, width=40)



build()
window.mainloop()

