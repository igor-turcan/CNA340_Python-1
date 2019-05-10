import turtle           #import the turtle module
import random           #import the random module

wn = turtle.Screen()            #create a screen
wn.bgcolor('lightblue')
wn.title("Turtle Race")         #label the screen

lance = turtle.Turtle()         #create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
                             #move the turtles to their starting point
andy.up()
lance.up()
andy.goto(-100, 20)         #make a random distance for andy to move
lance.goto(-100, -20)       #make a random distance for lance to move

start = turtle.Turtle()  # OPTIONAL-        #create a third object called start that will be used to display the winner of the game
start.hideturtle()                          #hide the third turtle object until the game is over for aesthetic purposes
lanceTotalDistance = 0
andyTotalDistance = 0

for i in range(150):            #iterate through the loop to run the forward method on both turtles 150 times

            #indent to begin the loop
            #use a cascading set of conditions to determine the winner

    andyDistance = random.randrange(1, 5)
    lanceDistance = random.randrange(1, 5)
    andy.forward(andyDistance)              #move andy forward and use the andyDistance variable to determine the amount to move forward by
    lance.forward(lanceDistance)            #move lance forward and use the lanceDistance variable to determine the amount to move forward by
    andyTotalDistance = andyTotalDistance + andyDistance
    lanceTotalDistance = lanceTotalDistance + lanceDistance
        #deindent to end the loop
        #use a cascading set of if conditions to determine the winner
for eachInt in range(145):          #indent to begin the loop
    if andyTotalDistance > lanceTotalDistance:          #this section is to determine the winner of the game and be used to print who the winner is. It calculates total distance for lance and for andy
        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
    elif lanceTotalDistance > andyTotalDistance:
        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
    else: print("Tie Game")
        #deindent to end the loop

wn.exitonclick()            #exit on click of the window
