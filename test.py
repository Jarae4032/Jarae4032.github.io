import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.screensize(500,300,"black")
wn.bgpic("52a33c10ae0c117156dd2807a4f324da.png")
wn.title("PacBeale")

#initialize turtle
bealepic = "pacBeale.gif"
wn.addshape(bealepic)
mazedrawer = trtl.Turtle()
mazerunner = trtl.Turtle(shape=bealepic)

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-500,380)
counter.pendown()
counter.color("white")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
font_setup = ("Arial", 20, "normal")
#Ghost Turtles

clyde = trtl.Turtle(shape="turtle")
clyde.penup()
clyde.color("orange")
clyde.goto(-90,20)

inky = trtl.Turtle(shape="turtle")
inky.penup()
inky.color("blue")
inky.goto(-30,20)

pinky = trtl.Turtle(shape="turtle")
pinky.penup()
pinky.color("pink")
pinky.goto(30,20)

blinky = trtl.Turtle(shape="turtle")
blinky.penup()
blinky.color("red")
blinky.goto(85,20)

# pellet turtles
pellet1 = trtl.Turtle(shape="circle")
pellet1.color("cornSilk")
pellet2 = trtl.Turtle(shape="circle")
pellet2.color("cornSilk")
pellet3 = trtl.Turtle(shape="circle")
pellet3.color("cornSilk")
pellet4 = trtl.Turtle(shape="circle")
pellet4.color("cornSilk")
pellet5 = trtl.Turtle(shape="circle")
pellet5.color("cornsilk")
pellet6 = trtl.Turtle(shape="circle")
pellet6.color("cornsilk")
pellet7 = trtl.Turtle(shape="circle")
pellet7.color("cornsilk")
pellet8 = trtl.Turtle(shape="circle")
pellet8.color("cornSilk")
pellet9 = trtl.Turtle(shape="circle")
pellet9.color("cornSilk")
pellet10 = trtl.Turtle(shape="circle")
pellet10.color("cornSilk")

# Barriers for the teleportation hallways
box1 = trtl.Turtle(shape="square")
box1.penup()
box1.color("black")
box1.goto(-500,20)
box1.turtlesize(2)

box2 = trtl.Turtle(shape="square")
box2.penup()
box2.color("black")
box2.goto(500,20)
box2.turtlesize(2)

# pellet placement
pellet1.penup()
pellet1.goto(140, 80)

pellet2.penup()
pellet2.goto(-170, 50)

pellet3.penup()
pellet3.goto(-240, -180)

pellet4.penup()
pellet4.goto(260, 190)

pellet5.penup()
pellet5.goto(-270, 80)

pellet6.penup()
pellet6.goto(0,210)

pellet7.penup()
pellet7.goto(170,-200)

pellet8.penup()
pellet8.goto(0,-300)

pellet9.penup()
pellet9.goto(-160,200)

pellet10.penup()
pellet10.goto(260,-140)


mazerunner.penup()
mazerunner.goto(0,-43)
mazerunner.color("yellow")


#Variables
angle = 90
path_width = 20
wall_length = path_width
# colors = ["blue","red","orange","pink","green","purple","black","brown","goldenrod","sienna","fuchsia"]
wall_thickness = 5
num_walls = 25
mze_wll_clr = "red"

def tmaze(x,y):
    mazedrawer.penup()
    mazedrawer.setheading(0)
    mazedrawer.goto(x,y)
    mazedrawer.pendown()
    mazedrawer.forward(115)
    mazedrawer.right(90)
    mazedrawer.forward(70)
    mazedrawer.back(70)
    mazedrawer.left(90)
    mazedrawer.forward(115)

def lmaze(x,y,f):
    mazedrawer.penup()
    mazedrawer.setheading(0)
    mazedrawer.goto(x,y)
    mazedrawer.pendown()
    mazedrawer.forward(f)

def ltmaze(x,y,r):
    mazedrawer.penup()
    mazedrawer.setheading(0)
    mazedrawer.goto(x,y)
    mazedrawer.pendown()
    mazedrawer.forward(300)
    if r == True:
        mazedrawer.goto(-210,-270)
        mazedrawer.setheading(90)
        mazedrawer.forward(70)
    elif r == False:
        mazedrawer.goto(215,-270)
        mazedrawer.setheading(90)
        mazedrawer.forward(70) 

def lsmaze(x,y,r):
    mazedrawer.penup()
    mazedrawer.setheading(0)
    mazedrawer.goto(x,y)
    mazedrawer.pendown()
    if r == True:
        mazedrawer.forward(80)
        mazedrawer.right(90)
        mazedrawer.forward(70)
    elif r == False:
        mazedrawer.setheading(180)
        mazedrawer.forward(80)
        mazedrawer.left(90)
        mazedrawer.forward(70)

def sdmaze(x,y):
    mazedrawer.penup()
    mazedrawer.setheading(270)
    mazedrawer.goto(x,y)
    mazedrawer.pendown()
    mazedrawer.forward(70)

def stmaze(x,y,r):
    mazedrawer.penup()
    mazedrawer.setheading(270)
    mazedrawer.goto(x,y)
    mazedrawer.pendown()
    if r == True:
        mazedrawer.forward(130)
        mazedrawer.goto(-210,115)
        mazedrawer.setheading(0)
        mazedrawer.forward(120)



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def go_up():
    mazerunner.setheading(90)
def go_down():
    mazerunner.setheading(270)
def go_left():
    mazerunner.setheading(180)
def go_right():
    mazerunner.setheading(0)            

def go_turtle():
    mazerunner.forward(1)
    # wn_canvas = wn.getcanvas()
    # x,y = mazerunner.position()
    # margin = 5
    # items = wn_canvas.find_overlapping(x+margin, -y+margin, x - margin, -y - margin)

    # if (len(items) > 0):
    #     canvas_color = wn_canvas.itemcget(items[0], 'fill')
    #     if canvas_color == mze_wll_clr:
    #         mazerunner.color('gray')
    #         wn.onkeypress(None, 'space')
    #         return
    wn.ontimer(go_turtle, 15)


#Setup for maze
mazedrawer.pensize(wall_thickness)
mazedrawer.color(mze_wll_clr)
mazedrawer.speed("fastest")

#Drawing the maze

# ghost box trace
mazedrawer.color(mze_wll_clr)
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(-55,60)
mazedrawer.pendown()
mazedrawer.forward(60)
mazedrawer.left(90)
mazedrawer.forward(80)
mazedrawer.left(90)
mazedrawer.forward(235)
mazedrawer.left(90)
mazedrawer.forward(80)
mazedrawer.left(90)
mazedrawer.forward(60)

# Outer top maze trace
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(495,50)
mazedrawer.pendown()
mazedrawer.forward(180)
mazedrawer.right(90)
mazedrawer.forward(70)
mazedrawer.right(90)
mazedrawer.forward(175)
mazedrawer.left(90)
mazedrawer.forward(205)
mazedrawer.left(90)
mazedrawer.forward(975)
mazedrawer.left(90)
mazedrawer.forward(205)
mazedrawer.left(90)
mazedrawer.forward(175)
mazedrawer.right(90)
mazedrawer.forward(70)
mazedrawer.right(90)
mazedrawer.forward(180)
mazedrawer.penup()
mazedrawer.setheading(-90)
mazedrawer.goto(0,325)
mazedrawer.pendown()
mazedrawer.forward(80)

# Outer bottom maze trace
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(-490,-10)
mazedrawer.pendown()
mazedrawer.forward(-180)
mazedrawer.left(-90)
mazedrawer.forward(-70)
mazedrawer.left(-90)
mazedrawer.forward(-175)
mazedrawer.right(-90)
mazedrawer.forward(-250)
mazedrawer.right(-90)
mazedrawer.forward(-975)
mazedrawer.right(-90)
mazedrawer.forward(-250)
mazedrawer.right(-90)
mazedrawer.forward(-175)
mazedrawer.left(-90)
mazedrawer.forward(-70)
mazedrawer.left(-90)
mazedrawer.forward(-180)
mazedrawer.penup()
mazedrawer.setheading(0)
mazedrawer.goto(-485,-205)
mazedrawer.pendown()
mazedrawer.forward(75)
mazedrawer.penup()
mazedrawer.setheading(180)
mazedrawer.goto(485,-205)
mazedrawer.pendown()
mazedrawer.forward(65)

# drawing the T-shaped sections of the maze
tmaze(-115,180)
tmaze(-115,-80)
tmaze(-115,-205)

# drawing the straight line sections of the maze
lmaze(-400,180,90)
lmaze(310,180,90)
lmaze(-220,-140,130)
lmaze(100,-140,130)
lmaze(-400,260,90)
lmaze(-220,260,120)
lmaze(100,260,120)
lmaze(310,260,90)

# drawing the long T-shaped sections of the maze
ltmaze(-400,-270,True)
ltmaze(100,-270,False)

# drawing the l shaped sections of the section
lsmaze(-400,-140,True)
lsmaze(400,-140,False)

# drawing the other straight sections of the maze
sdmaze(-210,-10)
sdmaze(220,-10)

# Drawing other t shaped sections of the maze
stmaze(-210,180,True)


# Ghost movement
clyde

# mazedrawer.hideturtle()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_turtle, "space")

wn.listen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()