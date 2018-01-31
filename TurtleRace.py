#Import the modules we need
import turtle
import random

#Create a screen

win = turtle.Screen()

#Draw a finish line
naychelle = turtle.Turtle()
naychelle.color("red")
naychelle.penup()
naychelle.goto(150,300)
naychelle.pendown()
naychelle.right(90)
naychelle.forward(500)

#Create two turtles and give them colors and turtle shape

peter = turtle.Turtle()
grace = turtle.Turtle()

peter.color("purple")
grace.color("lightblue")

peter.shape("turtle")
grace.shape("turtle")

#Move the turtles to their starting positions
peter.penup()
grace.penup()

peter.goto(-200,-10)
grace.goto(-200, 10)

peter.pendown()
grace.pendown()

#Send them racing across the screen

x_grace = grace.xcor()
x_peter = peter.xcor()

while x_grace and x_peter < 150:
    speed0 = random.randrange(1,10)#random speed--new each time
    speed1 = random.randrange(1,10)
    
    peter.speed(speed0)
    grace.speed(speed1)
    
    distance0 = random.randrange (-1,70)#random distance each time
    distance1 = random.randrange (-1,70)
    
    peter.forward(distance0)
    x_peter = peter.xcor()  #Update how far Peter went
    if x_peter >= 150:      #stop running if someone crosses the finish line
        break
    
    grace.forward(distance1)
    x_grace = grace.xcor() #Update how far Grace went
    if x_grace >= 150:     #stop running if someone crosses the finish line
        break
    
        

win.exitonclick()