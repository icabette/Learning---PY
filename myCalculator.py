from tkinter import *
from decimal import *

# Key input def
def click(key):
    display.insert(END, key)

# main
window = Tk()
window.title("My Calculator")

# top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=W)

# updatable entry widget
display = Entry(top_row, width=45, background="light green")
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
    Button(num_pad, text=btn_text, width=5, command=click(btn_text)).grid(row=r,column=c)
    c = c+1
    if c > 2:\
        c = 0
        r = r+1

# GUI main loop
window.mainloop()