# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hello, and welcome to my game!."

    e "I've been waiting for someone to talk to." 

    e "Will you talk to me?"

    e "Do you want to talk inside or outside?."

    menu:
        "go outside":
            jump outside

        "stay in this room.":
            jump stay

label outside: 

    scene bg whitehouse with dissolve
    show eileen concerned

    e "It's freezing out here!"
    e "Lets go inside where it's warm"
    return

label stay:

    show eileen happy

    e "*Phew*"
    e "It's a lot warmer in here"
    return