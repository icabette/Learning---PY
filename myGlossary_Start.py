# myGlossary_Start.py

from tkinter import *

# Key input function
def click():
    entered_text = entry.get()
    output.delete(0.0, END)
    definition = my_glossary[entered_text]
    output.insert(END, definition)

### main
window = Tk()
window.title("My Coding Club Glossary")
window.geometry("640x480")

# Label
Label(window, text="Please enter your searching word:").grid(row=0, column=0, sticky=W)

# Text entry widget
entry = Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# Add submit button
Button(window, text="Submit", width=5, command=click).grid(row=2,column=0,sticky=W)

# Other label
Label(window, text="\nDefine:").grid(row=3, column=0, sticky=W)

# Create Text Box
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# Dictionary
my_glossary = {
    'Algorithm':'Computer logic to perform specific action',
    'Bug':'Cause of unexpected action of program',
    'Binary':'Binary number'
}

### loop main
window.mainloop();