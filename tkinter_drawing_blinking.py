from time import sleep
from tkinter import *

window = Tk()
window.title("Drawing Test")
window.geometry("803x602")
window.resizable(False, False)

canvas=Canvas(window,width="803", height="602", relief="solid", bg="black", bd=1)

def drawGrid():
    canvas.create_line(0,201,803,201,fill="green")
    canvas.create_line(0,402,803,402,fill="green")
    canvas.create_line(201,0,201,602,fill="green")
    canvas.create_line(402,0,402,602,fill="green")
    canvas.create_line(603,0,603,602,fill="green")

def drawRect(blink):
    baseX = 31
    baseY = 31
    rSize = 140
    offsetX = 0
    offsetY = 0
    color = "blue"
    if blink == 1:
        color = "black"
    while(1):
        if offsetX > 800:
            offsetX = offsetX - 802
            offsetY = offsetY + 201
        canvas.create_rectangle(baseX+offsetX,baseY+offsetY,baseX+offsetX+rSize,baseY+offsetY+rSize,fill=color)
        offsetX = offsetX + 602

        if offsetY > 600:
            break

def drawRectMove(show):
    baseX = 31
    baseY = 31
    rSize = 140
    offsetX = 0
    offsetY = 0
    fcolor = "blue"
    bcolor = "black"
    for i in range (0,12):
        if offsetX > 800:
            offsetX = offsetX - 802
            offsetY = offsetY + 201
        if show == i:
            canvas.create_rectangle(baseX+offsetX,baseY+offsetY,baseX+offsetX+rSize,baseY+offsetY+rSize,fill=fcolor)
        else:
            canvas.create_rectangle(baseX+offsetX,baseY+offsetY,baseX+offsetX+rSize,baseY+offsetY+rSize,fill=bcolor)
        window.update()
        offsetX = offsetX + 201
        if offsetY > 600:
            break

canvas.pack()
drawGrid()
while (1):
    for i in range(0,12):
        drawRectMove(i)
        #sleep(0.5)
window.mainloop()