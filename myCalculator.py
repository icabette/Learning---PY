from dis import dis
from ipaddress import collapse_addresses
from tkinter import *
from decimal import *
from turtle import right, st

# Key input def
def click(key):
    # case of "="
    if key == "=":
        try:
            result = str(eval(display.get()))
            display.insert(END, " = " + result)
        except:
            display.delete(0,END)
            display.insert(END, " >> Error!")
    elif key == "C":
        display.delete(0, END)
    else:
        display.insert(END, key)

# main
window = Tk()
window.title("My Calculator")

# top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=W)

# updatable entry widget
display = Entry(top_row, width=45, background="light green", justify="right")
display.grid()

# num pad frame
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

# list of num pad number
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]

# loop for creating btn
r = 0
c = 0

for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# operator frame
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

# list of operator
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C'
]

# loop for creating btn
r = 0
c = 0

for btn_text in operator_list:
    def optCmd(key = btn_text):
        click(key)
    Button(operator, text=btn_text, width=5, command=optCmd).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

"""
lastRow = Frame(window)
lastRow.grid(row=2, column=0, columnspan=2, sticky=W)

Button(lastRow, text="", width=45).grid(row=0, column=0)
"""

# GUI main loop
window.mainloop()