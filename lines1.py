#Importing

import turtle
import time


#Setup the screen

scr = turtle.Screen()
scr.title("Lines in Engg. Drawings By Sk Akram with python")
scr.setup(width=1000, height=700)
scr.bgcolor("White")


#Function

def create_turtle():
    global t
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.penup()
    t.goto(-300,0)
    t.pendown()

def create_pen(y,heading,info):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("Black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 170)
    pen.write(f"{heading}", align= "center",
    font=("Curier",24,"bold"))
    pen.penup()
    pen.goto(0, y)
    pen.color("yellow")
    pen.write(f"{info}", align="center", font=("Curier", 15,"italic"))
    time.sleep(5)
    scr.clear()


def drawing1():
    global t,scr
    create_turtle()
    t.width(5)
    t.speed(1)
    t.fd(600)
    create_pen(y= 100,heading= "Continous Wide Line", info= "Applications: \nVisible edges and outlines")


def drawing2():
    global t,scr
    create_turtle()
    t.width(2)
    t.speed(1)
    t.fd(600)
    create_pen(y= -170,heading= "Continous Narrow Line", 
    info="Applications:\n1.Dimension,Extension & projection lines,\n2.Hatching lines for cross sections,\n3.Leader & Reference lines,\n4.Imaginary lines of Intersection,\n5.Short Centric lines,\n6.Bending lines")


def drawing3():
    global t,scr
    create_turtle()
    t.width(5)
    t.speed(5)

    for i in range(15):
        t.setheading(270)
        t.circle(10, -180)
        t.circle(-10, -180)
    create_pen(y=100, heading="Continous Narrow Irregular line", 
    info="Applications: \nLimits of partial views \nor sections provided the line is not an axis")
    

def drawing4():
    global t,scr
    create_turtle()
    t.width(2)
    t.speed(1)
    for i in range(30):
        t.fd(10)
        t.up()
        t.fd(10)
        t.down()
    create_pen(y=100, heading="Dasheds Narrow line", info="Applications: \nHidden outlines and Edges.")


def drawing5():
    global t,scr
    create_turtle()
    t.width(2)
    t.speed(1)

    for i in range(19):
        t.fd(15)
        t.up()
        t.fd(10)
        t.down()
        t.dot()
        t.up()
        t.fd(10)
        t.down()
    create_pen(y=-170, heading="Long Dashed dotted narrow line", info="Applications:\n1.Centre Lines,\n2.Lines of Symmetry,\n3.Pitch Circle for Gears.\n4.Pitch Circle for Holes. ")

def drawing6():
    global t,scr
    create_turtle()
    t.width(5)
    t.speed(1)

    for i in range(17):
        t.fd(20)
        t.up()
        t.fd(10)
        t.down()
        t.dot(5)
        t.up()
        t.fd(10)
        t.down()
    create_pen(y=-170, heading= "Long Dashed dotted wide line", info="Applications: \nSurfaces Which have to meet special requirement.")

def drawing7():
    global t,scr
    create_turtle()
    t.up()
    t.goto(-300,-100)
    t.speed(1)

    def das():
        global t
        for i in range(3):
            t.width(2)
            t.fd(20)
            t.up()
            t.fd(10)
            t.dot()
            t.up()
            t.fd(10)
            t.down()
    def wide_das():
        global t
        t.down()
        t.width(7)
        t.fd(20)
        t.up()
        t.fd(10)
        t.down()
    
    for i in [1,0,1]:
        wide_das()
        t.dot(7)
        t.up()
        t.fd(10)
        t.down()
        das()
        wide_das()
        t.setheading(90*i)
        t.down()
    create_pen(y=-170, heading= "Long dashed dotted narrow line with \nwide line at Ends", info= "Applications: \nCutting Planes")

def drawing8():
    global t,scr
    create_turtle()
    t.speed(1)
    t.width(5)
    for i in range(7):
        t.fd(35)
        t.up()
        t.fd(15)
        for i in range(2):
            t.dot()
            t.up()
            t.fd(15)
            t.down()

    create_pen(y=-190, heading= "Long Dashed Double dotted", 
    info= "Applications: \n1.Preformed outlines,\n2.Adjacent parts,\n3.Extreme position of movable parts,\n4.Initial outlines priorto forming,\n5.Outline of Finished parts.\n6.Project tolerence Zones.")


def drawing9():
    global t,scr
    create_turtle()
    t.speed(1)
    t.width(2)
    t.fd(80)
    for i in range(6):
        t.left(90)
        t.fd(40)
        t.right(150)
        t.fd(40*2)
        t.left(150)
        t.fd(34)
        t.right(90)
        t.fd(80)
    create_pen(y=-190, heading= "Continuous Straight Narrow line with Zig-Zag", 
    info= "Applications: \nLimits of partial or interrupted views.")

#Main loop    

for function in [drawing1(), drawing2(), drawing3(), drawing4(), drawing5(), drawing6(), drawing7(), drawing8(), drawing9()]:
    global t
    function

create_pen(y= 100, heading= "Thank You",info= "by Sk Akram")



scr.exitonclick()

