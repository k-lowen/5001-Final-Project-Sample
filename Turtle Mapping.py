# import package and making object
import turtle

pen = turtle.Turtle()



# method to draw square with dots
# space --> distance between dots
# x     --> side of square
def starting_map(space, quadrant_size):
    pen.speed(1000)
    for i in range(quadrant_size):
        for j in range(quadrant_size):
            # dot
            pen.dot()

            # distance for another dot
            pen.forward(space)
        pen.backward(space * quadrant_size)

        # direction
        pen.right(90)
        pen.forward(space)
        pen.left(90)

    # Main Section


pen.penup()
starting_map(10, 30)

# hide the turtle
pen.hideturtle()
