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



image andrew_logo = "gui/andrew.png"


# The game starts here.
label splashscreen:
    play music "audio/Vanguard_Heart.mp3" fadein 1.0 loop
    scene black
    with Pause(1) 
    show andrew_logo at center with dissolve
    show text "Andrew management studio" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    return

label start:
    define player_name = "Alex"
    call classroom

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
    play music "audio/Vanguard_Heart.mp3" fadein 1.0 loop
    "I can't believe I am finally here. The University of Vanguard Pirates. This is where I will learn to become a great pirat--.."
    play sound "audio/Bump.mp3"
    
    unknown "\"Whoa! That was a pretty solid hit. You okay?\""
    
    show cappy_happy at pos3
    "I rub my head and look up to see a tall, muscular Capybara mink with a friendly smile."
    
    "He definetly looks familiar..."
    "Wait a second..."
    "\"Cappy?\""
    cappy "\"Huh?\""

    # Show cappy thinking

    cappy "\"You know my name? I don't think we've met before.\""

    "\"Seriously? After all that time in South Blue Prep?\""
    "I don't think he remembers me..."
    "To be fair, we were never really close friends, but we did hang out a few times."
    "Your vision clears up and you notice that he is standing in the middle of a group of people"

    "To the left a blonde haired woman"

    show iris_happy at pos1

    if player_pronouns == "female":
        unknown "Hey. Are you ok?"
        $ affection["iris"] += 1
    
    unknown "Your lucky you didn't bump into and hurt my Reiji"
    
    "The blonde woman leans against the tall dark skinned man beside her on her right"
    
    show reiji_neutral at pos2

    reiji "Iris, baby girl. I'm fine."
    iris "Just making sure your ok, my Reiji-kins"

    "Your vision goes to the right and you notice a shy man who looks like a nerd and he smells bad, like trash"

    show trasher_neutral at pos5

    unknown "Oh, hi down there. Names..."
    unknown "Well, you can just call me Trasher"
    "Trasher?"
    "..."
    "What kind of name is that?" 
    trasher "You need some help getting up? I bet my robotic arm could get you up real quick"

    "To the imediate right of Capy is a large man who looks like he is going to talk to you about why we need communism"

    show newt_happy at pos4
    
    if player_pronouns == "non-binary":
        unknown "You known this person Cappy?"
    elif player_pronouns == "male":
        unknown "You known this guy Cappy?"
    else:
        unknown "You know this gal Cappy?"
    
    cappy "Maybe? I'm not sure Newt"

    "Newt turns and looks down at you"

    newt "Let me tell you about why we need communism"

    iris "Shut up Newt. No one wants to hear another of your stupid speeches"

    newt "awwwwwwww"

    "You focus back at Cappy and say..."

    menu:
        "We went to school together at South Blue Prep":
            $ affection["cappy"] += 1
            "I awkwardly explain that we went to school together at South Blue Prep."
            cappy "\"Ermm... South Blue? I must have hit my head harder than I thought.\""
            cappy "\"I'm sorry, I am kinda bad with faces. Especially old ones.\""
        "Nevermind, must've been someone else":
            $ affection["cappy"] -= 1
            "I decide to let it go and say it must have been someone else."
            cappy "\"Oh, okay. Sorry about that. I guess I am just a bit forgetful.\""
    
    "Cappy smiles and offers a handshake."
    cappy "\"Well, it's nice to meet you anyway. I'm Cappy D. Bara\""
    "I shake his hand and introduce myself... again."
    "\"It's nice to meet you, Cappy. I'm [player_name].\""
    cappy "\"Nice to meet you too, [player_name]... wait I think I do remember you from somewhere.\""
    cappy "\"Didn't you go to South Blue Prep?\""
    "Didn't I just say that? I guess he is a bit forgetful."
    "\"Yeah, I did. I guess you don't remember me that well.\""
    cappy "\"Sorry about that. I guess I am just a bit forgetful.\""
    "Cappy smiles and pats me on the back."
    "\"Well it was nice to see you again Cappy but I should probably get to class now. First class is at 8AM and I don't want to be late.\""
    cappy "\"Oh you're actually going to class? I thought you were just here to hang out.\""
    "Huh, what does he mean by that? This is a university, of course I am going to class."
    cappy "\"I'm staying out here, about to light my third cigarette of the day. I don't really go to class much.\""
    "I guess I should have expected that from him. He was never really the studious type."
    cappy "\"But hey, if you ever want to skip class and hang out, just let me know. I can show you around the campus and we can grab some food or something. Maybe even smoke a joint with me or something.\""
    menu:
        "Go To Class":
            "I politely decline his offer and tell him I need to get to class."
            "\"Thanks for the offer Cappy, but I really need to get to class. I don't want to be late on my first day.\""
            cappy "\"Oh, okay. I understand. Maybe we can hang out later then?\""
            "Yeah maybe, if he even remembers me."
            jump classroom

        "Skip Class":
            "I decide to skip class and hang out with Cappy."
            "\"You know what? I think I will skip class and hang out with you for a bit.\""
            cappy "\"Really? Awesome! I promise you won't regret it. I know all the best spots on campus.\""
            "Cappy smiles and leads me away from the school gate."
            jump school_track

label classroom:
    scene black with fade
    image classroom = im.Scale("images/scenes/classroom.png", 1920, 1280)
    scene classroom with fade

    "This classroom reminds me of the one I had in South Blue Prep. It has the same old wooden desks and chalkboard."

    "There are a few students already here, chatting and laughing, but not very many seats left. I guess I should find a seat before the class starts."
    menu:
        "Sit in the front row":
            jump newt_class1
            
            return

        "Sit in the back row":
            jump yomi_class1

    show fenton_happy at pos3 with dissolve
    fenton "Welcome to the University, [player_name]. I am Professor Fenton, your first year advisor."
    fenton "I will be teaching you about the history of the Vanguard Pirates and how to become a great pirate."
    
    "Wow, this is going to be an interesting class. I can't wait to learn more about the Vanguard Pirates."
    
    return

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

    "You get closer to them and notice the blonde woman and dark skinned man from at the gate"

    scene school_track with fade

    show iris_happy at pos1 with dissolve
    show reiji_neutral at pos2 with dissolve

    iris "Oh its [them] from the gate, you better stay away from my boyfriend"
    reiji "Calm down babe, you know I'm all yours"
    
    return