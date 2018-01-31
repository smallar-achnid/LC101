#Get some turtles
import turtle
peter = turtle.Turtle()

def draw_square(length):
    for i in range (4):
        peter.forward(length)
        peter.left(90)
        
#draw foursquare
def draw_foursquare():
    #repeat the following four times:
    for i in range (4):
        #draw one square
        draw_square(100)
        #turn 90 degrees to the right
        peter.left(90)
            
#draw the wagon wheel
def wagon_wheel(number_of_foursquare):
    #repeat the following number_of_foursquare times:
    for i in range(number_of_foursquare):
        #draw foursquare
        draw_foursquare()
        #turn it to the desired angle (180/(number_of_foursquare))
        peter.left(180/((number_of_foursquare)*2))
        
number_of_foursquare = input("How many foursquares would you want to use to draw the wagon wheel?")
number_of_foursquare = int(number_of_foursquare)
wagon_wheel(number_of_foursquare)