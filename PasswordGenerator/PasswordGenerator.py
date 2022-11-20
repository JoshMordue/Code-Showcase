import tkinter as tk

window = tk.Tk()
window.title('Password Generator')
window.geometry('500x500')

description = tk.Label(window, bg='white', width=50, height='5', text="This application is for generating passwords.\n"
                                                                  "Please select from the checkboxes below your preferences")
description.pack()



op1 = tk.Checkbutton(window, text='Lowercase', variable='', onvalue=1, offvalue=0)
op2
op3


window.mainloop()

