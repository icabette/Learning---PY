from tkinter import *
from turtle import bgcolor
from time import sleep

canvas_height = 800
canvas_width = 1280
canvas_colour = "black"

p1_x = canvas_width/2
p1_y = canvas_height
p1_colour = "red"
line_width = 5
line_length = 5

###### function

# user control
def p1_move_N(event):
    global p1_y
    
    canvas.create_line(p1_x,p1_y,p1_x, (p1_y-line_length),width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length

def p1_move_S(event):
    global p1_y
    
    canvas.create_line(p1_x,p1_y,p1_x, (p1_y+line_length),width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length

def p1_move_W(event):
    global p1_x
    
    canvas.create_line(p1_x,p1_y,(p1_x-line_length), p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length

def p1_move_E(event):
    global p1_x
    
    canvas.create_line(p1_x,p1_y,(p1_x+line_length), p1_y,width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length

def erase_all(event):
    global p1_x, p1_y
    
    canvas.delete(ALL)
    p1_x = canvas_width/2
    p1_y = canvas_height

###### main code
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(200,50,400,250,fill="blue")
canvas.create_oval(800,50,1000,250,fill="yellow")
canvas.create_polygon(600,250,500,450,700,450,fill="orange")

# while(1):
#     canvas.create_oval(800,50,1000,250,fill="black")
#     window.update()
#     sleep(1)
#     canvas.create_oval(800,50,1000,250,fill="yellow")
#     window.update()
#     sleep(1)

# key reaction
window.bind("<Up>",p1_move_N)
window.bind("<Down>",p1_move_S)
window.bind("<Left>",p1_move_W)
window.bind("<Right>",p1_move_E)
window.bind("u", erase_all)

window.mainloop()