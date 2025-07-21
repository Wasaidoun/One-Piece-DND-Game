# The script is the script for our Vanguard Pirates one piece dnd game as a University dating sim

# Declare characters used by this game. The color argument colorizes the
# name of the character.




#Happy images size for characters to be called upon

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

    call prologue

    # This is the school gate background scene
    # Used the same image scale as the characters for full screen

    image school_gate = im.Scale("images/scenes/school_gate.png", 1920, 1280)

    scene school_gate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show iris_happy at pos1
    show reiji_neutral at pos2
    show trasher_neutral at pos3
    show newt_happy at pos4
    show cappy_happy at pos5

    iris "Reiji, You're here"
    reiji "Course I'm here, baby girl"
    trasher "I like trash"
    newt "Yooooooooooo, Cappyyyyyyyyyyyyy"
    cappy "Yo whats cookin good lookin. You ready to start this class [player_name]?"

    if player_pronouns == "non-binary":
        newt "I heard [they] are a real badass, I like that in a person"
    else:
        newt "I heard [they] is a real badass, I like that in a person"


    # This ends the game.
    return
