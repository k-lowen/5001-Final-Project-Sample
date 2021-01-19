import turtle

def decision_one_right(turtle, direction):
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(350, 200)
    turtle.dot()
    turtle.speed(1)
    turtle.pendown()
    turtle.width(10)
    turtle.right(180)
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


    if direction == "right":
        turtle.goto(300, 200)
        turtle.pendown()
        turtle.right(180)
        turtle.forward(55)
        turtle.dot()
        good_choice(turtle)
        #turtle is now at 300, 255
    elif direction == "left":
        turtle.color("red")
        turtle.goto(300, 200)
        turtle.pendown()
        turtle.forward(50)
        yikes(turtle)

def correct_decision_one(turtle):
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(350, 200)
    turtle.pendown()
    turtle.dot()
    turtle.speed(1)
    turtle.width(10)
    turtle.right(180)
    turtle.forward(50)
    turtle.dot()
    turtle.right(90)
    turtle.forward(50)
    turtle.dot()

    # turtle is now at 300,250

def decision_two_right(turtle, direction):
    correct_decision_one(turtle)
    turtle.color("green")
    turtle.dot()
    turtle.penup()
    turtle.goto(300, 250)
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
    turtle.goto(300, 250)

    if direction == "right":
        turtle.pendown()
        turtle.color("green")
        turtle.dot()
        turtle.width(10)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(200)
        good_choice(turtle)
        #turtle is now at 160, 270

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
    turtle.width(10)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(200)
    turtle.dot()
    #turtle is now at 160, 270

def decision_three_left(turtle, direction):
    correct_decision_2(turtle)
    turtle.color("blue")
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

    turtle.goto(160, 270)
    turtle.width(10)
    turtle.pendown()

    if direction == "left":
        turtle.color("blue")
        turtle.dot()
        turtle.right(180)
        turtle.forward(120)
        turtle.dot()
        good_choice(turtle)
        #turtle location 160, 150

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
    #turtle is at location 160,150

def decision_four_right(turtle, direction):
    correct_decision_three(turtle)
    turtle.color("orange")
    turtle.dot()
    turtle.width(3)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(180)

    #turtle at 160, 220

    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(160, 150)
    turtle.width(10)
    turtle.color("orange")

    if direction == "left":
        turtle.color("red")
        turtle.dot()
        turtle.left(180)
        #in a square
        for i in range(4):
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.dot()
        yikes(turtle)

        #turtle os now at 160,150

    elif direction == "right":
        turtle.color("orange")
        turtle.pendown()
        for i in range(3):
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(40)
            turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    good_choice(turtle)

    # turtle at 70,220

    #add portal options

def correct_decision_four(turtle):
    correct_decision_three(turtle)
    turtle.color("orange")
    turtle.dot()
    turtle.right(90)
    for i in range(3):
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.dot()

    # turtle at 70, 220


def decision_five_left(turtle, direction):
    correct_decision_four(turtle)
    turtle.color("purple")
    turtle.dot()
    turtle.right(90)
    turtle.forward(30)
    turtle.dot()
    turtle.width(3)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)

    for i in range(10):
        turtle.color("pink")
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(40, 220)
    turtle.color("purple")
    turtle.width(10)
    turtle.pendown()
    turtle.dot()


    if direction == "left":
        turtle.dot()
        turtle.color("purple")
        turtle.forward(55)
        turtle.dot()
        good_choice(turtle)
        #turtle now at 40, 165

    elif direction == "right":
        turtle.color("red")
        turtle.right(180)
        turtle.forward(55)
        turtle.dot()
        yikes(turtle)
    #ADD ELSE/ACCIDENTAL PORTAL TO HOUSE 2

def correct_decision_five(turtle):
    correct_decision_four(turtle)
    turtle.color("purple")
    turtle.dot()
    turtle.right(90)
    turtle.forward(85)

    turtle.dot()
    # turtle now at -15, 220

def decision_six_left(turtle, direction):
    correct_decision_five(turtle)
    turtle.color("light blue")
    turtle.dot()
    turtle.left(90)

    for i in range(3):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)

    turtle.forward(30)

    #turtle at 70, 75

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

    turtle.goto(15, 130)
    turtle.width(10)
    turtle.color("light blue")
    turtle.pendown()

    if direction == "left":
        #turtle at 15, 130
        turtle.dot()
        turtle.left(90)
        turtle.forward(130)
        turtle.right(90)
        turtle.forward(15)
        turtle.color("light blue")
        turtle.dot()
        celebrate(turtle)

    if direction == "right":
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
    turtle.write("Nice choice!", font = style, align = "right")

def yikes(turtle):
    turtle.color("red")
    style = ("Comic Sans", 100, "bold")
    turtle.write("uh oh...", font = style, align = "right")





#DECISION %
#CORRECT DECISION 5
#DECISION 6



def welcome(turtle):
    turtle.color("red")
    style = ("Comic Sans", 100, "bold")
    turtle.write("Welcome Home...", font = style, align = "center")












def main():
    house_turtle = turtle.Turtle()
    background_colour = "black"
    house_turtle.shape("turtle")

    window = turtle.Screen()
    window.bgcolor(background_colour)

    #welcome(house_turtle)
    window.exitonclick()




    house_turtle.speed(2)
    house_turtle.width(10)



    #correct_decision_one(house_turtle)
    #correct_decision_2(house_turtle)
    #correct_decision_three(house_turtle)
    #correct_decision_four(house_turtle)
    #correct_decision_five(house_turtle)
    #decision_one_right(house_turtle, "right")
    #decision_two_right(house_turtle, "right")
    #decision_three_left(house_turtle, "right")
    #decision_four_right(house_turtle, "right")
    #decision_five_left(house_turtle, "right")
    #decision_six_left(house_turtle, "left")






    window.exitonclick()

main()