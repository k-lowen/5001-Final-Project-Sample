import turtle

def decision_one_left(turtle, direction):
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(-300, 300)
    turtle.dot()
    turtle.speed(1)
    turtle.pendown()
    turtle.width(10)
    turtle.right(90)
    turtle.forward(50)
    turtle.dot()
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.width(3)


    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.color("yellow")
    turtle.width(10)


    if direction == "left":
        turtle.goto(-300, 250)
        turtle.pendown()
        turtle.forward(55)
        turtle.dot()
        good_choice(turtle)
        #turtle is now at -245,250
    elif direction == "right":
        turtle.color("red")
        turtle.goto(-300, 250)
        turtle.pendown()
        turtle.right(180)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(60)
        yikes(turtle)

def correct_decision_one(turtle):
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(-300, 300)
    turtle.dot()
    turtle.speed(1)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.goto(-300, 250)
    turtle.pendown()
    turtle.forward(55)
    turtle.dot()
    # turtle is now at -245,250

def decision_two_right(turtle, direction):
    correct_decision_one(turtle)
    turtle.color("green")
    turtle.dot()
    turtle.penup()
    turtle.goto(-245, 250)
    turtle.width(3)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.pendown()
    #now draw dotted line
    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)
    #return to position to make decision
    turtle.goto(-245,250)

    if direction == "right":
        turtle.pendown()
        turtle.color("green")
        turtle.dot()
        turtle.width(10)
        turtle.forward(100)
        turtle.dot()
        good_choice(turtle)
        #turtle is now at -245, 150

    elif direction == "left":
        turtle.color("red")
        turtle.pendown()
        turtle.width(10)
        turtle.color("red")
        turtle.left(180)
        turtle.forward(55)
        yikes(turtle)
        #wrong decision so is sent to another place
        #add portal option

def correct_decision_2(turtle):

    correct_decision_one(turtle)
    turtle.color("green")
    turtle.dot()
    turtle.right(90)
    turtle.forward(100)
    turtle.dot()
    #turtle is now at -245, 150

def decision_three_left(turtle, direction):
    correct_decision_2(turtle)
    turtle.color("blue")
    turtle.dot()
    turtle.width(3)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(180)

    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(-245, 150)
    turtle.width(10)
    turtle.pendown()

    if direction == "left":
        turtle.color("blue")
        turtle.dot()
        turtle.forward(120)
        turtle.dot()
        good_choice(turtle)
        #turtle location -125, 150

    elif direction == "right":
        turtle.color("red")
        turtle.left(180)
        turtle.forward(50)
        yikes(turtle)

def correct_decision_three(turtle):
    correct_decision_2(turtle)
    turtle.color("blue")
    turtle.dot()
    turtle.left(90)
    turtle.forward(120)
    turtle.dot()
    #turtle is at location -125, 150

def decision_four_left(turtle, direction):
    correct_decision_three(turtle)
    turtle.color("orange")
    turtle.dot()
    turtle.width(3)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(180)

    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(-125, 150)
    turtle.width(10)
    turtle.color("orange")

    if direction == "left":
        turtle.color("orange")
        turtle.dot()
        turtle.left(180)
        turtle.pendown()
        turtle.forward(55)
        turtle.dot()
        good_choice(turtle)

        #turtle os now at -125, 205

    elif direction == "right":
        turtle.color("red")
        turtle.pendown()
        turtle.forward(55)
        yikes(turtle)

    #add portal options

def correct_decision_four(turtle):
    correct_decision_three(turtle)
    turtle.color("orange")
    turtle.dot()
    turtle.left(90)
    turtle.pendown()
    turtle.forward(55)
    turtle.dot()


def decision_five_right(turtle, direction):
    correct_decision_four(turtle)
    turtle.color("purple")
    turtle.dot()
    turtle.width(3)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(180)

    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(-125, 205)
    turtle.color("purple")
    turtle.width(10)
    turtle.pendown()
    turtle.dot()


    if direction == "right":
        turtle.dot()
        turtle.color("purple")
        turtle.forward(55)
        turtle.dot()
        good_choice(turtle)
        #turtle now at -70, 205

    elif direction == "left":
        turtle.color("red")
        turtle.left(180)
        turtle.forward(55)
        turtle.dot()
        yikes(turtle)
    #ADD ELSE/ACCIDENTAL PORTAL TO HOUSE 2

def correct_decision_five(turtle):
    correct_decision_four(turtle)
    turtle.color("purple")
    turtle.dot()
    turtle.right(90)
    turtle.forward(55)
    turtle.dot()

def decision_six_right(turtle, direction):
    correct_decision_five(turtle)
    turtle.color("light blue")
    turtle.dot()
    turtle.width(3)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(180)

    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(-70, 205)
    turtle.width(10)
    turtle.color("light blue")
    turtle.pendown()

    if direction == "right":
        turtle.dot()
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(65)
        turtle.color("light blue")
        turtle.dot()
        celebrate(turtle)

    if direction == "left":
        turtle.color("red")
        turtle.left(180)
        turtle.forward(55)
        yikes(turtle)

def celebrate(turtle):
    turtle.color("yellow")
    style = ("Comic Sans", 100, "bold")
    turtle.write("GOAL!!", font = style, align = "center")

def good_choice(turtle):
    turtle.color("lime green")
    style = ("Comic Sans", 50, "italic")
    turtle.write("Nice choice!", font = style, align = "left")

def yikes(turtle):
    turtle.color("red")
    style = ("Comic Sans", 100, "bold")
    turtle.write("uh oh...", font = style, align = "center")





#DECISION %
#CORRECT DECISION 5
#DECISION 6















def main():
    space_turtle = turtle.Turtle()
    background_colour = "black"
    turtle_colour_space = "red"

    window = turtle.Screen()
    window.bgcolor(background_colour)


    space_turtle.shape("turtle")

    space_turtle.speed(2)
    space_turtle.width(10)



    #correct_decision_one(space_turtle)
    #correct_decision_2(space_turtle)
    #
    #correct_decision_three(space_turtle)
    #correct_decision_four(space_turtle)
    #correct_decision_five(space_turtle)
    #decision_one_left(space_turtle, "left")
    #decision_two_right(space_turtle, "right")
    #decision_three_left(space_turtle, "right")
    #decision_four_left(space_turtle, "left")
    #decision_five_right(space_turtle, "right")
    #decision_six_right(space_turtle, "right")






    window.exitonclick()

main()