from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
x0 = 10		# initial left-most edge of ball
y0 = 50		# initial top-most edge of ball
x1 = 60		# inital right-most edge of ball
y1 = 100	# you've probably got the idea by now.
dx = 2
dy = 3
# create ball:
which = canvas.create_oval(x0,y0,x1,y1,fill="blue", tag='blueBall')
while True:
    canvas.move('blueBallx, dy')
    canvas.after(20)
    canvas.update()
# the next 4 if statements check if the ball hits a wall: if it hits
# a floor/ceiling its y-velocity reverses and it if hits a left/right 
# wall its x-velocity reverses
    if x1 >= 400:
        dx = -2
    if x0 = 300:
        dy = -3
    if y0 < 0:
        dy = 3
    x0 += dx
    x1 += dx
    y0 += dy
    y1 += dy
window.mainloop()
