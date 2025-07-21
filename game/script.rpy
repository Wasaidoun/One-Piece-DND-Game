# The script is the script for our Vanguard Pirates one piece dnd game as a University dating sim

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Dargg")
define i = Character("Iris")
define r = Character("Reiji")
define c = Character("Cappy D. Bara")
define t = Character("Trasher")
define n = Character("Newt")


#Happy images size for characters to be called upon

image iris_happy = im.Scale("iris happy.png", 607, 687)
image cappy_happy = im.Scale("cappy happy.png", 607, 687)
image newt_happy = im.Scale("newt happy.png", 607, 687)

#Neutral images size for characters to be called upon

image reiji_neutral = im.Scale("reiji neutral.png", 607, 687)
image trasher_neutral = im.Scale("trasher neutral.png", 607, 687)


#This is for the positioning of characters in a scene. From left to right 1-5. Tried 8 but doesn't really work with image sizes

transform pos1:     #Left
    xalign -0.10
    yalign 1.0
    

transform pos2:     #Middle Left
    xalign 0.20
    yalign 1.0
    

transform pos3:     #Center
    xalign 0.50
    yalign 1.0
    

transform pos4:     #Middle Right
    xalign 0.80
    yalign 1.0
    

transform pos5:     #Right
    xalign 1.10
    yalign 1.0
    



# The game starts here.

label start:

    # This is the school gate background scene
    # Used the same image scale as the characters for full screen

    image school_gate = im.Scale("school gate.png", 1920, 1280)

    scene school_gate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show iris_happy at pos1
    show reiji_neutral at pos2
    show trasher_neutral at pos3
    show newt_happy at pos4
    show cappy_happy at pos5

    i "Reiji, You're here"
    r "Course I'm here, baby girl"
    t "I like trash"
    n "Yooooooooooo, Cappyyyyyyyyyyyyy"
    c "Yo whats cookin."


    # This ends the game.
    return
