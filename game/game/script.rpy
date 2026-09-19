init:
    image eileen_happy = "images/eileen_happy.png"
    image eileen_concerned = "images/eileen_concerned.png"
    image bg whitehouse = "mist+dense.png"
    image bg room = "pra_a1_day1.png" 
    image bg death = "wallpaper2you_150233.jpg"

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

    show eileen_happy

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
    show eileen_concerned

    e "It's raining out here!"
    e "Lets go inside where it's warm and dry."
    jump stay

label stay:

    scene bg room with dissolve
    show eileen_happy

    e "*Phew*"
    e "It's a lot warmer in here. Let's talk."

    menu:
        "What do you want to talk about?":
            jump nervous

        "How.. how did I get here? what did you say about a game?":
            jump dissmissive
label dissmissive:

    scene bg death
    e "DONT ASK QUESTIONS YOU DON'T WANT THE ANSWERS TO"
    return

label nervous:

    show eileen_concerned

    e "I... don't know. I've been alone for so long, I don't know what I should talk about."
    e "*quietly* You won't leave me, right?"
    e "*shakes her head* Never mind. I'll enjoy however much time I get with you."

    show eileen_happy

    e "What should we do?"
    e "Do you want to watch a movie?"
    jump request

label request:

    scene bg room

    show eileen_happy
    menu:
        "Yes":
            jump movie 
        "No.":
            jump death

label death:

    scene bg death
    e "YOU SHOULDN'T HAVE SAID NO TO ME."
    e "LET'S TRY THAT AGAIN"
    jump request

label movie:
    return


