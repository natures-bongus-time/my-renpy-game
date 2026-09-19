init:
    image eileen_happy = "images/eileen_happy.png"
    image eileen_concerned = "images/eileen_concerned.png"
    image bg whitehouse = "mist+dense.png"
    image bg room = "pra_a1_day1.png" 
    image bg death = "wallpaper2you_150233.jpg"
    $ points = 0

define e = Character("Eileen", color="#c8ffc8")
define f = Character("???", color="#0e0c01")




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

    e "OH MY GOD!!!!!"

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

        "You. This is your fault. Because of you, I'm trapped here. What did you hope to accomplish?":
            jump dissmissive
label dissmissive:

    scene bg death
    f "DONT ASK QUESTIONS YOU DON'T WANT THE ANSWERS TO"
    f "WE'll PRETEND YOU DIDN'T SAY THAT, BUT I'LL BE WATCHING YOU."
    $ points += 1 
    jump nervous
    

label nervous:

    scene bg room with dissolve
    show eileen_concerned

    e "I... don't know. I've been alone for so long, I don't know what I should talk about."
    e "*quietly* You won't leave me, right?"

    menu:
        "*Laughs* Of course I will. Like THEY left you. Like everyone you ever loved left you. It's always been your fault, you know that right? Like with Sa-":
            $ points +=5
            jump better
        "I won't. I promise.":
            jump better

label better:

    if points >= 3: 
        return

    e "*shakes her head* Never mind. I'll enjoy however much time I get with you."

    show eileen_happy

    e "What should we do?"
    e "Do you want to watch a movie?"
    jump request

label request:

    scene bg room

    show eileen_happy
    if points >=3:
        return
    menu:
        "Yes":
            jump movie 

        "Why not.":
            jump movie

        "I'd love to!":
         $ points -= 1

        "With a pathetic freak like you? ew. Get away from me.":
            jump death

label request2:
    scene bg room
    
    show eileen_happy
    if points >=3:
            return
    menu:
        "Yes":
            jump movie 
    
        "Why not.":
            jump movie
    
        "I'd love to!":
            $ points -= 1
            jump movie

    
label death:

    scene bg death
    f "YOU SHOULDN'T HAVE SAID NO TO HER."
    f "LET'S TRY THAT AGAIN"
    $ points += 1
    jump request2

label movie:

    return


