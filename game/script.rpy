# The script is the script for our Vanguard Pirates one piece dnd game as a University dating sim



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

    show expression Text("Day 1", size=60, color="#ffffff", xalign=0.5, yalign=0.5) as day_label
    with dissolve

    pause 2

    hide day_label
    with dissolve

    call prologue

    # This is the school gate background scene
    # Used the same image scale as the characters for full screen

    image school_gate = im.Scale("images/scenes/school_gate.png", 1920, 1280)

    scene school_gate with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show iris_happy at pos1 with dissolve
    iris "Reiji, You're here"

    show reiji_neutral at pos2 with dissolve
    reiji "Course I'm here, baby girl"

    show trasher_neutral at pos3 with dissolve
    trasher "I like trash"

    show newt_happy at pos4 with dissolve
    newt "Yooooooooooo, Cappyyyyyyyyyyyyy"
    
    show cappy_happy at pos5 with dissolve
    cappy "Yo whats cookin good lookin."

    "The Capy Bara looking guy seems to notice you trying to get through"

    cappy "Oh, you trying to get through, sorry. Let me move out of your way. I'm Cappy btw, I'm a chill guy"

    menu:
        "Go To Class":
            jump school_hallway

        "Skip Class":
            jump school_track


label school_hallway:

    scene black with fade

    image school_hallway = im.Scale("images/scenes/school_hallway.png", 1920, 1280)

    scene school_hallway with fade

    "Your first class was fine, but as you are making your way to your next class a big man is in the way"

    show newt_happy at pos3 with dissolve
    newt "Oh hey, I remember you at the gate. I'm Newt. Captain of the Vanguard Club"
    newt "Let me tell you about why we need communism"

    # This ends the game.
    return


label school_track:

    scene black with fade

    image school_track = im.Scale("images/scenes/school_track.png", 1920, 1280)

    "You decide to skip class and head out behind the school to the track. Outside you see two figures in the distance"

    "You get closer to them and notice is the blonde woman and dark skinned man from at the gate"

    scene school_track with fade

    show iris_happy at pos1 with dissolve
    show reiji_neutral at pos2 with dissolve

    iris "Oh its [them] from the gates, you better stay away from my boyfriend"
    reiji "Calm down babe, you know I'm all yours"
    
    return