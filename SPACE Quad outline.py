import turtle
from SPACE_TURTLE import decision_one_left

#MAZE KEY:
# SPACE 1 LEFT (L to space 2, R stay in space 1 )
# SPACE 2 RIGHT (R- to space 3,L -- back to SPACE 1, Portal to house, ship, cabin)
# SPACE 3 LEFT (L/R)
# SPACE 4 LEFT (L, S, R, Portal)
# SPACE 5 RIGHT (RESET, R)
# SPACE 6 LEFT (L/R)
def simple_menu():
    print("Choose Wisely:")
    print("1. Left -- enter -- left ")
    print("2. Right -- enter -- right\n\n")

def object_menu(user_name):
    script = "Yikes, that looks like it could cause some damage, " + user_name
    print(script, "\n")
    print("1. Pick Up")
    print("2. Leave it. You've got more important things to worry about")

def portal_decision_menu():
    print("Honestly, these all look like bad options...")
    print("1. Left -- enter -- left")
    print("2. Right -- enter -- right")
    print("3. Portal -- enter -- portal \n\n")

def portal_menu():
    print("Careful! All portals are dangerous!")
    print("1. PORTAL TO THE HOUSE -- enter: house")
    print("2. PORTAL TO THE SHIP  -- enter: ship")
    print("3. PORTAL TO THE WOODS -- enter: woods")
    print("4. PORTAL TO THE GALAXY-- enter: galaxy \n\n")

def space_one(user_name):
    ''' function: first decision in Space Dimension, correct direction is Left
        parameters: one user input of string
        return: if direction is L, plays video and advances, else right is stuck in a loop'''

    print("Choices can be life or death. \nNo matter what, they've all got consequences \n")

    simple_menu()
    direction = input("Make your move: \n").lower()

    if direction == "left":
        #advances towards decision 2

        print("Nice work, lets keep moving\n\n")
        #decision_one_left(turtle,"left")
        print("[PLAY VIDEO]")
        space_two(user_name)

    else:
        #PLAY VIDEO
        print("[TURTLE GRAPHIC]")
        print("[PLAY VIDEO TO JUMP SCARE]")
        #this is a dead end, must choose another option
        print("Looks like you've got another shot " + user_name + ". Try again\n")
        space_one(user_name)

def space_two(user_name):
    #This is a portal -- Can jump to Q2 in House, Water, or Woods dimension
    #Choosing Right, advance to decision 3
    #choosing left, resets back to decision 1
    #choosing portal transports to other functions
    '''function: portal decision
        parameter: one direction input (str)
        returns: if L, loops to  D1, if R, advances to D3, else portal to other dimension D2'''

    portal_decision_menu()
    direction = input("Enter your chosen consequence: \n").lower()

    if direction == "right":
        #this choice advances the user to decision 3
        print("[INSERT FIRST and SECOND TURTLE GRAPHIC!!!")
        print("[PLAY VIDEO]")
        print("Looks like you're doing well...good luck\n\n")
        space_three(user_name)

    elif direction == "left":
        #keeps user in space 2
        print("[PLAY KNOCK OUT VIDEO")
        print("Glad to see you're up again. That didn't seem to work like we hoped...")
        space_two(user_name)

    elif direction == "portal":
        portal_menu()
        portal_choice = input("Choose your portal destination: \n").lower()

        #Call function for this decision house D2
        if portal_choice == "woods":
            print("PORTAL TO WOODS D2")
            print("TURTLE GRAPH")
            #call function for this decision woods D2
        elif portal_choice == "ship":
            print("PORTAL TO SHIP D2")
            print("TURTLE GRAPH")
            #call function for this decision ship D2
        elif portal_choice == "house":
            print("PORTAL TO HOUSE D2")
            print("TURTLE GRAPH")
            house_two(user_name)
        elif portal_choice == "galaxy":
            print("Luckily you're already here.")
            space_two(user_name)
        else:
            print("Looks like a typo, you'll regret that.")
            space_two(user_name)

    else:
        print("Looks like you chose an option that doesn't exist...")
        print("[PLAY KNOCK OUT VIDEO")
        print("Glad to see you're up again")
        space_two(user_name)

def space_three(user_name):
    #user advances if choice is left
    #if user chooses RIGHT, user is sent back to space 1
    #could potentially turn into another portal to D1 somewhere else

    simple_menu()
    direction = input("Trust your gut: \n").lower()

    if direction == "left":
        #user will advance to D4 Space
        print("Let's get a move on")
        print("TURTLE GRAPHIC")
        print("[PLAY VIDEO]\n\n")
        print("Nice work! Sure doesn't look like it is getting easier any time soon... \n\n")
        space_four(user_name)

    elif direction == "right":
        #knock out video and sent to Space D1
        print("Oh no. This doesn't look good for you")
        print("KNOCK OUT VIDEO OR NOT AND PLAY SPACE D1 Video")
        space_one(user_name)
    else:
        print("Looks like you chose an option that doesn't exist...")
        print("[PLAY KNOCK OUT VIDEO")
        print("Glad to see you're up again...Looks like you'll get another shot. Try to choose correctly this time \n\n")
        space_three(user_name)

def space_four(user_name):
    '''function: D4 for Space Dimension, is a portal to ship, woods, house D4
    :parameter: direction and user name
    returns: depending on choice, portals to other dimension or advances to D5 Space, or loops on itself'''

    # left advances to space D5
    # right loops back to space 4
    # portal to ship, woods, or house

    simple_menu()
    direction = input("Good luck...You'll need it. \n\n").lower()

    if direction == "left":
        print("[PLAY VIDEO  AND ADVANCE TO D5]")
        print("That was close, good call\n\n")
        space_five(user_name)

    elif direction == "right":
        print("Watch out!")
        print("[play knock out video]")
        print("Ouch! Hopefully that knocked all the bad decisions out. \n\n")
        space_four(user_name)

def space_five(user_name):
    '''function: Decision 5 in space dimension
        parameters: one direction (str)
        returns: if left is chosen, accidental portal to HOUSE D2, right advances to question 6'''

    simple_menu()

    direction = input("Nearly there! I have a feeling there is a nasty surprise somewhere around here... \n\n").lower()

    if direction == "left":
        print("Uh Oh...WATCH OUT!")
        print("[PLAY VIDEO OF PORTAL]")
        print("Looks like you hit a secret portal and are headed to the house...\n\n")
        #ENTER FUNCTION CALL TO HOUSE D2

    elif direction == "right":
        print("[PLAY VIDEO]")
        print("Woah, that could've been the end...")
        print("Lucky for you, you're nearly to safety. Keep going!\n \n")
        space_six(user_name)

    else:
        print("We can't have mistakes like that! Type like the world might end! \n\n")
        space_five(user_name)

def space_six(user_name):
    '''function: if user chooses L advances to GOAL, if R, loops back to 6, portal to woods,ship,or house D5
    parameters: one direction
    returns: choice of direction'''

    portal_decision_menu()
    direction = input("Last chance. Choose wisely: \n").lower()

    if direction == "left":
        print("[PLAY VIDEO]")
        print("You've completed your mission!")

    elif direction == "right":
        print("[PLAY VIDEO]")
        print("Ouch, that didn't work. Try again and this time choose the right one! \n\n")
        space_six(user_name)

    elif direction == "portal":
        portal_menu()
        portal_choice = input("Choose your dimension: \n").lower()
        if portal_choice == "woods":
            #CALL Woods 5 function
            print("[PLAY VIDEO AND MOVE TO WOODS 5]")
        elif portal_choice == "house":
            #call house 5 function
            print("[PLAY VIDEO AND CALL HOUSE 5]")
        elif portal_choice == "ship":
            #CALL ship 5 function
            print("[PLAY VIDEO AND CALL SHIP 5}")
        elif portal_choice == "galaxy":
            print("Good news. You're already here. Brains like that and you might be here a while...\n\n")
            space_six(user_name)
        else:
            print("Yikes! That wasn't an option! One more mistake like that and you're toast! \n\n")
            space_six(user_name)
    else:
        print("Yikes! That wasn't an option! One more mistake like that and you're toast! \n\n")
        space_six(user_name)









def main():
    #MUST CONNECT PORTALS AND D5 PORTAL TO HOUSE D2
    # Add text about what a portal can do? Play three clips to give spoilers?

    user_name = input("Enter your name: \n")
    print("Welcome to SPACE -- ADD IN MORE \n")

    space_one("Katie")

    space_turtle = turtle.Turtle()
    background_colour = "black"
    turtle_colour_space = "red"

    window = turtle.Screen()
    window.bgcolor(background_colour)
    window.exitonclick()


    space_turtle.shape("turtle")

    space_turtle.speed(2)
    space_turtle.width(10)
















    #print("[PLAY ENTRANCE VIDEO]\n \n")
    #play entrance video


    #space_one(user_name)


    #print("[PLAY VIDEO]")
    #print("GOALLLLLLL!")








main()