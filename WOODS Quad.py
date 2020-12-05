#HOUSE MAZE KEY
# Woods D1 -- Down
# Woods D2 --Up (or portal)
# Woods D3 -- Down
# Woods D4 -- up (or portal)
# Woods D5 -- down (up --> surprise portal to water D2)
# Woods D6 -- up

#CHANGE MENUS TO THEME


def simple_menu():
    print("1. Upstairs -- enter -- up")
    print("2. Downstairs -- enter -- down")

def stair_portal_menu():
    print("1. Upstairs -- enter -- up")
    print("2. Downstairs -- enter -- down")
    print("3. Portal -- enter -- portal \n\n")

def portal_decision_menu():
    print("Honestly, these all look like bad options...")
    print("1. Upstairs -- enter -- up")
    print("2. Downstairs -- enter -- down")
    print("3. Portal -- enter -- portal \n\n")

def portal_menu():
    print("Careful! All portals are dangerous!")
    print("1. PORTAL TO THE HOUSE -- enter: house")
    print("2. PORTAL TO THE SHIP  -- enter: ship")
    print("3. PORTAL TO THE WOODS -- enter: woods")
    print("4. PORTAL TO THE GALAXY-- enter: galaxy \n\n")

def woods_one(user_name):
    ''' function: first decision in woods Dimension, correct direction is UP
            parameters: one user input of string
            return: if direction is UP, plays video and advances, else DOWN is stuck in a loop'''

    simple_menu()
    direction = input("Let's get out of here!\n").lower()


    if direction == "up":
        #stuck in a loop at woods 1
        print("[PLAY VIDEO]")
        print("TURTLE GRAPH")
        print("Ouch, that was rough! Maybe we should try something else...\n")
        woods_one(user_name)

    elif direction == "down":
        #advances to woods 2
        print("Phew, that could've been bad...lets go")
        print("[PLAY VIDEO]")
        print("TURTLE GRAPH")
        woods_two(user_name)

    else:
        print("We can't be making silly typing mistakes at a time like this! \n\n")
        print("PLAY KNOCK OUT VIDEO")
        woods_one(user_name)

def woods_two(user_name):
    #correct direction is UP
    #down is a surprise portal to space D2
    #portal to any D2

    print("This is spooky, I think I hear something coming from upstairs... \n\n")
    stair_portal_menu()
    direction = input(" Should we go check it out? \n\n").lower()

    if direction == "up":
        print("Good call, watch out for the creaky steps...\n")
        print("[PLAY VIDEO WALKING UPSTAIRS]")
        print("TURTLE")
        #insert turtle graphic
        woods_three(user_name)

    elif direction == "down":
        print("Let's hide...")
        print("JUMP SCARE PORTAL TO WATER D2]")
        #insert turtle graphic
        #function call to space D2
        #space_two(user_name)

    elif direction == "portal":
        portal_menu()
        portal_choice = input("Choose your portal: \n\n")
        if portal_choice == "woods":
            print("Luckily you're already here.")
            print("TURTLE GRAPH")
            woods_two(user_name)
        elif portal_choice == "ship":
            print("PORTAL TO SHIP D2")
            print("TURTLE GRAPH")
            #call function for this decision ship D2
        elif portal_choice == "house":
            print("PORTAL TO HOUSE D2")
            #house_two(user_name)
            print("TURTLE GRAPH")
        elif portal_choice == "galaxy":
            print("PORTAL TO GALAXY D2")
            #space_two(user_name)
        else:
            print("Looks like a typo, you'll regret that.")
            woods_two(user_name)
    else:
        print("Looks like you chose an option that doesn't exist...")
        print("[PLAY KNOCK OUT VIDEO")
        print("Glad to see you're up again")
        woods_two(user_name)

def woods_three(user_name):
    #correct decision is DOWN

    simple_menu()
    direction = input("Yikes, this doesn't feel right...should we keep going or head downstairs?\n").lower()

    if direction == "up":
        print("[PLAY KNOCK OUT VIDEO]")
        print("[Turtle]")
        woods_three(user_name)

    elif direction == "down":
        print("[PLAY WALKING DOWNSTAIRS VIDEO]")
        print("TURTLE GRAPHIC")
        woods_four(user_name)

    else:
        print("[KNOCK OUT]")
        print("A typo like that and it could cost you...")
        woods_three(user_name)



def woods_four(user_name):
    #if DOWN, loops back to woods 3
    #if up advances to woods D5
    #if portal, portals to D4 in another quadrant

    print("Is it just me, or did you see something moving over there...\n\n")

    stair_portal_menu()
    direction = input("Which way should we go? \n\n").lower()

    if direction == "up":
        print("Good call, watch out for the creaky steps...\n")
        print("[PLAY VIDEO WALKING UPSTAIRS]")
        print("TURTLE")
        # insert turtle graphic
        woods_five(user_name)

    elif direction == "down":
        print("Lets get a move on. Keep your eyes down...\n")
        print("JUMP SCARE call woods D3 ")
        # insert turtle graphic
        woods_four(user_name)

    elif direction == "portal":
        portal_menu()
        portal_choice = input("Choose your portal: \n\n")
        if portal_choice == "woods":
            print("Luckily you're already here.")
            print("TURTLE GRAPH")
            woods_four(user_name)
            # call function for this decision woods D4
        elif portal_choice == "ship":
            print("PORTAL TO SHIP D4")
            print("TURTLE GRAPH")
            # call function for this decision ship D4
        elif portal_choice == "house":
            print("PORTAL TO HOUSE D4")
            print("TURTLE GRAPH")
            #house_four(user_name)
        elif portal_choice == "galaxy":
            print("PORTAL TO GALAXY D4")
            #function call galaxy D4
            #space_four(user_name)

        else:
            print("Looks like a typo, you'll regret that.")
            woods_four(user_name)
    else:
        print("Looks like you chose an option that doesn't exist...")
        print("[PLAY KNOCK OUT VIDEO")
        print("Glad to see you're up again")
        woods_four(user_name)


def woods_five(user_name):
    #correct choice is DOWN
    #if chooses UP, accidental portal to house D2

    print("I can feel us getting close! This could be make or break so choose wisely...\n\n")
    simple_menu()

    direction = input("Which was should we go?\n").lower()

    if direction == "down":
        #Advance to woods D6
        print("Let's get moving")
        print("[PLAY GOING UPSTAIRS VIDEO]")
        print("TURTLE GRAPHIC")
        woods_six(user_name)

    elif direction == "up":
        #accidental portal to house D2
        print("Let's go...\n")
        print("[PLAY VIDEO]")
        print("uh oh...this doesn't look good...\n\n")
        #FUNCTION CALL house D2
        #house_two(user_name)
    else:
        print("yikes, typos like that and we are done for...\n")
        woods_four(user_name)

def woods_six(user_name):
    #last stop in woods dimension
    #correct choice is UP
    #if chooses down, loops to woods d4

    print("We are getting close! Stay focused and let's get out of here! \n\n")

    simple_menu()
    direction = input("Which way to safety? \n").lower()

    if direction == "up":
        print("[PLAY VIDEO OF ENDING ]")
        print("GOALLLLL")

    elif direction == "down":
        print("stay quiet and watch out for creaky steps \n\n")
        print("PLAY VIDEO OF KNOCK OUT")
        woods_four(user_name)

    else:
        print("yikes, typos like that and we are done for...\n")
        woods_six(user_name)


def main():

    user_name = input("Enter your name...\n")
    woods_one(user_name)





main()
