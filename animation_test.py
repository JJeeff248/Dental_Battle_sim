import time
from tkinter import *

root = Tk()

canvas = Canvas(root, width=1920 , height= 1080)
canvas.pack()

dude_img = PhotoImage(file="dude.png")

##canvas.create_line(0, 0, 200, 100)
##canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
##
##canvas.create_rectangle(50, 25, 150, 75, fill="blue")

wave = canvas.create_image(400, 400, anchor = CENTER, image=dude_img)


while True:
    for i in range(0, 10):
        canvas.move(1, 0, -5)
        root.update()
        time.sleep(0.02)

    for i in range(0, 10):
        canvas.move(1, 0, 5)
        root.update()
        time.sleep(0.02)


