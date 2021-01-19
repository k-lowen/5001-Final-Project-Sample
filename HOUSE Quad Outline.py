from moviepy.editor import *
import pygame

#HOUSE MAZE KEY
# ENTRANCE -- ENTER
# HOUSE D1 -- GO
# HOUSE D2 -- GO
# HOUSE D3 -- RIGHT
# HOUSE D4 -- LISTEN
# HOUSE D5 -- LEFT
# HOUSE D6 -- RECEPTION

#MENU FUNCTIONS

def decision_one_menu(user_name):

    print("Something feels off...should we go looking?\n")
    print("Choose wisely, ", user_name, ".\n")
    print("0. Quit -- enter -- quit")
    print("1. Let's Go-- enter -- go")
    print("2. Let's Stay -- enter -- stay")


def decision_two_menu(user_name):

    print("Seems suspicious, be safe, ", user_name, ".\n")
    print("0. Quit -- enter -- quit")
    print("1. Let's go and find Mom -- enter -- go")
    print("2. Not a chance, get us out of here -- enter -- leave\n")


def decision_three_menu(user_name):

    print( user_name, ", Things are getting weird fast.\n")
    print("0. Quit -- enter -- quit")
    print("1. Let's try the door on the right -- enter -- right")
    print("2. Not a chance, we are going left -- enter -- left\n")


def decision_four_menu(user_name):

    print( user_name, ", she seems off. Maybe she has some information, should we listen or try another room?\n")
    print("0. Quit -- enter -- quit")
    print("1. Hear what she has to say? -- enter -- listen")
    print("2. Try a different room -- enter -- leave\n")


def decision_five_menu(user_name):

    print(user_name, " there might be something in the dresser... let's go find it. \n")
    print("0. Quit -- enter -- quit")
    print("1. Left -- enter -- left")
    print("2. Right -- enter -- right\n")


def decision_six_menu(user_name):

    print(user_name, " this sounds suspicious. A reception?! Should we investigate? \n")
    print("0. Quit -- enter -- quit")
    print("1. Follow her to the reception -- enter -- reception")
    print("2. Keep looking around -- enter -- explore\n")


def stair_portal_menu():
    print("0. Quit -- enter -- quit")
    print("1. Upstairs -- enter -- up")
    print("2. Downstairs -- enter -- down")
    print("3. Portal -- enter -- portal \n\n")


def entrance_menu():
    print("0. Quit -- enter -- quit")
    print("1. Enter -- enter -- enter")


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


def entrance_video():
    pygame.display.set_caption('Where next?')

    clip = VideoFileClip('Where have you been?.mp4')
    clip.preview()

    pygame.quit()


#VIDEO FUNCTIONS
def decision_one_video():
    try:
        pygame.display.set_caption("decision one")

        clip = VideoFileClip('Decision 1 Clip.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def decision_two_video():
    try:
        pygame.display.set_caption("decision two")

        clip = VideoFileClip('Nell Walks to room.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def decision_three_video():
    try:
        pygame.display.set_caption("decision three")

        clip = VideoFileClip('Nell Finds Her Mom.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def decision_four_video():
    try:
        pygame.display.set_caption("decision four")

        clip = VideoFileClip('Nell Goes to Get Dressed.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def decision_five_video():
    try:
        pygame.display.set_caption("decision five")

        clip = VideoFileClip('Nell Opens Dresser.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def decision_six_video():
    try:
        pygame.display.set_caption("decision five")

        clip = VideoFileClip('Nell dresses and mom enters.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def final_video():
    try:
        pygame.display.set_caption("ending")

        clip = VideoFileClip('Reception Dance.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


def knock_out_video():
    try:
        pygame.display.set_caption("knock out")

        clip = VideoFileClip('Knock Out Video.mp4')
        clip.preview()

        pygame.quit()
    except(FileNotFoundError, FileNotFoundError):
        print("There is an error playing this video")


#START AND END FUNCTIONS
def end_of_game(user_name):
    print("Thanks for playing!", user_name, " come back soon!")

def entrance(user_name, file_output):
    '''function: enter or quit the game
        parameters: one input
        returns: start or end game'''

    entrance_menu()

    try:
        direction = input("Choose now: \n").lower()

        if direction == "enter" or direction == "1":
            file_writing(file_output, direction)
            entrance_video()
            house_one(user_name, file_output)

        elif direction == "quit" or direction == "0":
            file_writing(file_output, direction)
            knock_out_video()
            end_of_game(user_name)

        else:
            file_writing(file_output, direction)
            entrance(user_name, file_output)

    except(TypeError):
        print("Looks like an invalid input!")
    except(ValueError):
        print("Tha isn't an option!")



#FILE WRITING FUNCTION
def file_writing(file_input, new_direction):
    try:
        if new_direction != "quit" or new_direction != "0":
            file_output = open("New Game -- ", "a")
            file_output.write(new_direction)
            file_output.write(" ")
            file_output.close()

        elif new_direction == "quit" or new_direction == "0":
            file_output = open("New Game -- ", "a")
            file_output.write("end")
            file_output.close()

    except(FileNotFoundError, FileExistsError, IOError):
        print("Looks like there is an error with the file")

def file_search(file_output, name):
    '''function: searches list of existing games
        parameters: file and name input
        returns: list of directions'''

    file_output = open("New Game -- ", "r")
    for line in file_output:
        name_list = line.split()
        if name_list[0] == name:
            print(name_list)


#DECISION/MAZE FUNCTIONS
def house_one(user_name, file_output):
    ''' function: first decision in House Dimension, correct direction is GO
            parameters: one user input of string
            return: if direction is STAY, plays video and advances, else is stuck in a loop'''
    #script
    print("\n")
    print("Welcome to the Haunted Mansion ", user_name, ". We have been waiting for you\n")
    print("Best of luck getting out of here...\n")

    decision_one_menu(user_name)

    #decision recursively calls next function

    try:
        direction = input("Should we start investigating or get out of here?\n").lower()

        if direction == "stay" or direction == "2":
            file_writing(file_output, direction)
            #stuck in a loop at house 1

            knock_out_video()
            print("TURTLE GRAPH")
            print("Ouch, that was rough! Maybe we should try something else...\n")
            house_one(user_name, file_output)

        elif direction == "go" or direction == "1":
            file_writing(file_output, direction)
            decision_one_video()
            print("Did you see that?! Weird.", user_name, ", stay alert until we figure out what is going on!\n")
            print("TURTLE GRAPH")
            #decision_one_right(house_turtle, "right")

            #next "level"
            house_two(user_name, file_output)

        elif direction == "quit" or direction == "0":
            file_writing(file_output, direction)
            end_of_game(user_name)

        else:
            house_one(user_name, file_output)

    except(TypeError):
        print("Looks like an invalid input type!")
    except(ValueError):
        print("Tha isn't an option!")


def house_two(user_name, file_output):
    ''' function: second decision in House Dimension, correct direction is GO
            parameters: one user input of string
            return: if direction is STAY, plays video and advances, else is stuck in a loop'''


    print("This is spooky, I think I hear something coming from inside that room... \n")
    decision_two_menu(user_name)

    try:
        direction = input(" Should we go check it out? \n\n").lower()

        if direction == "go" or direction == "1":
            file_writing(file_output, direction)
            print("Good call, watch out for the creaky floorboards...\n")
            decision_two_video()
            print("TURTLE")
            #insert turtle graphic
            house_three(user_name, file_output)

        elif direction == "leave" or direction == "2":
            file_writing(file_output, direction)
            print("Let's hide...")
            knock_out_video()
            house_two(user_name, file_output)
            #insert turtle graphic


        elif direction == "quit" or direction == "0":
            file_writing(file_output, direction)
            end_of_game(user_name)

        else:
            print("Looks like you chose an option that doesn't exist...")
            file_writing(file_output, direction)
            knock_out_video()
            # print("Glad to see you're up again")
            house_two(user_name, file_output)

    except(TypeError, ValueError):
        print("Oops! Looks like something went wrong!")

    # #elif direction == "portal":
    #     portal_menu()
    #     portal_choice = input("Choose your portal: \n\n")
    #     if portal_choice == "woods":
    #         print("PORTAL TO WOODS D2")
    #         print("TURTLE GRAPH")
    #         #call function for this decision woods D2
    #     elif portal_choice == "ship":
    #         print("PORTAL TO SHIP D2")
    #         print("TURTLE GRAPH")
    #         #call function for this decision ship D2
    #     elif portal_choice == "house":
    #         print("Luckily you're already here.")
    #         print("TURTLE GRAPH")
    #         house_two(user_name)
    #     elif portal_choice == "galaxy":
    #         print("PORTAL TO GALAXY D2")
    #         #space_two(user_name)
    #     else:
    #         print("Looks like a typo, you'll regret that.")
    #         house_two(user_name)


def house_three(user_name, file_output):
    ''' function: third decision in House Dimension, correct direction is LEFT
            parameters: one user input of string
            return: if direction is RIGHT, plays video and advances, else is stuck in a loop'''


    decision_three_menu(user_name)
    direction = input("This doesn't feel right...what should we do??\n").lower()

    try:
        if direction == "left" or direction == "2":
            file_writing(file_output, direction)
            knock_out_video()
            print("[Turtle]")
            house_three(user_name, file_output)

        elif direction == "right" or direction =="1":
            file_writing(file_output, direction)
            decision_three_video()
            print("TURTLE GRAPHIC")
            house_four(user_name, file_output)

        elif direction == "quit" or direction == "0":
            file_writing(file_output, direction)
            end_of_game(user_name)

        else:
            file_writing(file_output, direction)
            knock_out_video()
            print("A typo like that and it could cost you...")
            house_three(user_name, file_output)

    except(TypeError, ValueError):
        print("Oops! Looks like something went wrong!")


def house_four(user_name, file_output):
    ''' function: fourth decision in House Dimension, correct direction is LISTEN
            parameters: one user input of string
            return: if direction is LEAVE, plays video and advances, else is stuck in a loop'''

    print("Is it just me, or did you see something moving over there...\n\n")

    decision_four_menu(user_name)
    direction = input("It is up to you. \n\n").lower()

    try:
        if direction == "listen" or direction == "1":
            file_writing(file_output, direction)
            print("Good call, watch out for the creaky steps...\n")
            decision_four_video()
            print("TURTLE")
            # insert turtle graphic
            house_five(user_name, file_output)

        elif direction == "leave" or direction == "2":
            file_writing(file_output, direction)
            print("Lets get a move on. Keep your eyes down...\n")
            knock_out_video()
            # insert turtle graphic
            house_four(user_name, file_output)

        elif direction == "quit" or direction == "0":
            file_writing(file_output, direction)
            end_of_game(user_name)

        # elif direction == "portal":
        #     portal_menu()
        #     portal_choice = input("Choose your portal: \n\n")
        #     if portal_choice == "woods":
        #         print("PORTAL TO WOODS D2")
        #         print("TURTLE GRAPH")
        #         # call function for this decision woods D4
        #     elif portal_choice == "ship":
        #         print("PORTAL TO SHIP D2")
        #         print("TURTLE GRAPH")
        #         # call function for this decision ship D4
        #     elif portal_choice == "house":
        #         print("Luckily you're already here.")
        #         print("TURTLE GRAPH")
        #         house_four(user_name)
        #     elif portal_choice == "galaxy":
        #         print("PORTAL TO GALAXY D2")
        #         #function call galaxy D4
        #         #space_four(user_name)
        #
        #     else:
        #         print("Looks like a typo, you'll regret that.")
        #         house_four(user_name)
        else:
            file_writing(file_output, direction)
            print("Looks like you chose an option that doesn't exist...")
            knock_out_video()
            print("Glad to see you're up again")
            house_four(user_name, file_output)

    except(TypeError, ValueError):
        print("Oops! Looks like something went wrong!")


def house_five(user_name, file_output):
    ''' function: fifth decision in House Dimension, correct direction is LEFT
            parameters: one user input of string
            return: if direction is RIGHT, plays video and advances, else is stuck in a loop'''


    print("Maybe she has something planned. Should we take her advice?\n")

    decision_five_menu(user_name)

    try:
        direction = input("Which was should we go?\n").lower()

        if direction == "left" or direction == "1":
            file_writing(file_output, direction)
            #Advance to house D6
            decision_five_video()
            decision_six_video()
            print("TURTLE GRAPHIC")

            house_six(user_name, file_output)

        elif direction == "right" or direction == "2":
            file_writing(file_output, direction)
            print("Let's go...\n")
            print("uh oh...this doesn't look good...\n\n")
            knock_out_video()
            house_five(user_name, file_output)


        elif direction == "quit" or direction == "0":
            file_writing(file_output, direction)
            end_of_game(user_name)

        else:
            file_writing(file_output, direction)
            print("yikes, typos like that and we are done for...\n")
            house_five(user_name, file_output)

    except(TypeError, ValueError):
        print("Oops! Looks like something went wrong!")

def house_six(user_name, file_output):
    ''' function: sixth decision in House Dimension, correct direction is RECEPTION
            parameters: one user input of string
            return: if direction is EXPLORE, plays video and advances, else is stuck in a loop'''


    decision_six_menu(user_name)

    try:

        direction = input("What does your gut say...? \n").lower()

        if direction == "reception" or direction == "1":
            file_writing(file_output, direction)
            final_ending(user_name)

        elif direction == "explore" or direction == "2":
            file_writing(file_output, direction)
            print("something is off... \n\n")
            knock_out_video()
            house_six(user_name, file_output)

        else:
            file_writing(file_output, direction)
            print("yikes, typos like that and we are done for...\n")
            house_six(user_name, file_output)

    except(TypeError, ValueError):
        print("Oops! Looks like something went wrong!")


def final_ending(user_name):
    print("Thank you for exploring the Haunted Mansion. Enjoy your eternal stay, ", user_name, ".")
    final_video()



def main():


    print("Do you wish to: ")
    print("1. Begin a new game -- enter -- new")
    print("2. View an old game -- enter -- old")

#GAME BEGINS

    try:
        user_game = input("Choose now: \n").lower()

        if user_game == "new" or user_game == "1":
            file_output = open("New Game -- ", "a")
            file_output.write("\n")
            user_name = input("Enter your name...\n")
            file_writing(file_output, user_name)
            entrance(user_name, file_output)

        elif user_game == "old" or user_game == "2":
            file_output = open("New Game -- ", "r")
            user_search = input("Would you like to search for a name? -- enter -- yes or no\n")
            if user_search == "yes":
                name_search = input("What name would you like to search? \n")
                file_search(file_output, name_search)
            else:
                file_output = open("New Game -- ", "r")
                for line in file_output:
                    single_line = line.split()
                    print(single_line)
        else:
            print("Oops! That wasn't an option!")

    except(FileNotFoundError, IOError):
        print("Oops! This file does not exist")


main()



















