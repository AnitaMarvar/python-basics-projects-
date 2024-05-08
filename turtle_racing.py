import turtle
import time
import random
WIDTH,HEIGHT=500,500  #all capitals constant denote karta hai
COLORS=['cyan','brown','black','red','blue','green','purple','yellow','orange','pink']

def get_number_of_racers():
    racers=0
    while True:
        racers=input("enter the number of racers(2-10): ")  #python takes input in the form of strings therefore it should be converted to int
        if racers.isdigit():
            racers=int(racers)
        else:
            print("input is not numeric...Try Again!")
            continue
#number nhi hai toh waapas loop chalega aur hum range mein hai kya dekhege
        if 2<=racers<=10:
            return racers
        else:
            print("Enter valid number")

            
def race(colors):
    turtles=create_turtle(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos() #gives the position of the turtle
            if y>=HEIGHT //2 -10:
                return colors[turtles.index(racer)]
#['blue','red']
# [turtle1,turtle2]
#    0        1
def create_turtle(colors):
     turtles=[]
     spacingx=WIDTH//(len(colors)+1)
     for i, color in enumerate(colors):  #enumerate gives index and values
         racer=turtle.Turtle()
         racer.color(color)
         racer.shape('turtle')
         racer.left(90)
         racer.penup()
         racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2+20 )
         racer.pendown()
         turtles.append(racer)
     return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing!")



racers=get_number_of_racers()
init_turtle()
random.shuffle(COLORS) #it gives us first color from colours
colors=COLORS[:racers]
#agar 2 racers hai toh 2 colors ka list return karega
#creating a new turtle object
winner=race(colors)
print("The winner is ",winner)
time.sleep(5)
# racer.speed(2)  #speed is between 0,10; 0 fastest 
# racer.penup()  #no line is drawn

# racer.color('cyan')
# racer.forward(100)
# time.sleep(15)  #pause for 5 secs