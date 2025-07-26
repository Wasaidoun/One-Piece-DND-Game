label day1_morning:
    play sound "audio/Alarm.mp3" fadein 0.5
    scene black
    with fade
    scene dorm_room
    
    with fade
    player "That alarm never gets any easier to wake up to. I guess I should get ready for the day."
    player "Wait, what time is it? I should probably check my phone."
    show phone
    with dissolve
    player "Oh no! It's already 7:50? Did I really sleep through all my alarms... I am going to be late for my first class! I need to hurry up and get dressed."
    hide phone with dissolve
    player "I quickly get dressed and grab my bag. I don't want to be late on my first day."
    player "I rush out of my dorm room and head to the university gates. I hope I can make it in time."
    scene school_gate
    with dissolve
    player"As I arrive at the university gates, I see a few other students heading to class. I guess I am not the only one running late."
    player "I take a deep breath and try to calm down. I can do this. It's just the first day, and I am sure everything will be fine."
    player "I walk through the gates and head towards the main building. I can see a few students chatting and laughing, but I am too focused on getting to class on time."
    scene school_hallway
    with dissolve
    player "Okay. Hall A. Room 318. I think that's the right place."
    player "Or maybe it's Hall B? I should have checked the map before I left."

    menu:
        "Look around for help":
            jump look_around_help
            "Ask someone for help"
        "Try to find it on your own":
            jump find_on_own

label find_on_own:
    player "Alright, I should probably ask someone for help. I don't want to be late on my first day and wandering around aimlessly won't help."
    play sound "audio/Bump.mp3" fadein 0.5
    show cappy_happy with dissolve
    cappy_unknown "\"Woah there, you took a sharp turn there. You almost bumped into me!\""
    "\"What do you mean almost? I did bump into you!\""
    cappy_unknown "\"Oh that was you? I thought it was just the wind. I wasn't really paying attention.\""
    player "I look at the guy I bumped into. He is a tall capybara with a muscular build and a friendly smile."
    player"He looks familiar, but I can't quite place him."
    player"Wait a second..."
    player "\"Cappy?\""
    cappy_unknown "\"Huh?\""
    # Show cappy thinking
    cappy "\"You know my name? I don't think we've met before.\""
    player "\"Seriously? After all that time in South Blue Prep?\""
    player "I don't think he remembers me..."
    player "To be fair, we were never really close friends, but we did hang out a few times."
    menu:
        "We went to school together at South Blue Prep":
            $ affection["cappy"] += 1
            player "I awkwardly explain that we went to school together at South Blue Prep."
            cappy "\"Ermm... South Blue? I must have hit my head harder than I thought.\""
            cappy "\"I'm sorry, I am kinda bad with faces. Especially old ones.\""
        "Nevermind, must've been someone else":
            $ affection["cappy"] -= 1
            player "I decide to let it go and say it must have been someone else."
            cappy "\"Oh, okay. Sorry about that. I guess I am just a bit forgetful.\""
    player "Cappy smiles and scratches his head."
    cappy "\"Well, it's nice to meet you anyway. I'm Cappy D. Bara\""
    player "I shake his hand and introduce myself... again."
    player "\"It's nice to meet you, Cappy. I'm [player_name].\""
    cappy "\"Nice to meet you too, [player_name]... wait I think I do remember you from somewhere.\""
    cappy "\"Didn't you go to South Blue Prep?\""   
    player "Didn't I just say that? I guess he is a bit forgetful."
    player "\"Yeah, I did. I guess you don't remember me that well.\""
    cappy "\"Sorry about that. I guess I am just a bit forgetful.\""
    "Cappy smiles and pats you on the back."
    player "\"Well it was nice to see you again Cappy but I should probably get to class now. First class is at 8AM and I don't want to be late.\""
    cappy "\"Oh you're actually going to class? I thought you were just here to hang out.\""
    player "Huh, what does he mean by that? This is a university, of course I am going to class."
    cappy "\"I'm staying out here, about to light my third cigarette of the day. I don't really go to class much.\""
    player "I guess I should have expected that from him. He was never really the studious type."
    player "\"Why are you smoking in the hallway? Isn't that against the rules?\""
    cappy "\"Oh, I don't really care about the rules. I just do what I want.\""
    player "I guess that explains why he is skipping class."
    cappy "\"But hey, if you ever want to skip class and hang out, just let me know. I can show you around the campus and we can grab some food or something. Maybe even smoke a joint with me or something.\""
    menu:
        "Go To Class":
            player "I politely decline his offer and tell him I need to get to class."
            player "\"Thanks for the offer Cappy, but I really need to get to class. I don't want to be late on my first day.\""
            cappy "\"Oh, okay. I understand. Maybe we can hang out later then?\""
            player "Yeah maybe, if he even remembers me."
            jump classroom

        "Skip Class":
            player "I decide to skip class and hang out with Cappy."
            player "\"You know what? I think I will skip class and hang out with you for a bit.\""
            cappy "\"Really? Awesome! I promise you won't regret it. I know all the best spots on campus.\""
            player "Cappy smiles and leads me away from the school gate."
            #jump skip_class
# Add a label for where they go to skip class
# label skip_class:

label classroom:
    scene black with fade
    
    scene classroom with fade

    player "This classroom reminds me of the one I had in South Blue Prep. It has the same old wooden desks and chalkboard."

    player "There are a few students already here, chatting and laughing, but not very many seats left. I guess I should find a seat before the class starts."
    player "I look around the room and see two empty seats. One in the third row..."
    show newt_happy
    newt_unknown "\"It's been a while since I've seen you man. *Gags*, I thought you would have at least tried to take a shower over the summer break.\""
    hide newt_happy
    show trasher_neutral
    trasher_unknown "\"Yeah! My doctor actually told me I am allergic to 99 percent of every soap on the market!\""
    hide trasher_neutral
    show yomi_happy
    yomi_unknown "\"...\""
    hide yomi_happy

    player "And one in the back row..."
    show reiji_neutral
    reiji_unknown "\"Hey baby girl, saved you a seat right here.\""
    hide reiji_neutral
    show iris_happy
    iris_unknown "\"Oh, thank you Reiji. You're so sweet.\""
    hide iris_happy
    
    menu:
        "Sit in the third row":
            player "I decide to sit in the third row."
            show newt_happy with dissolve
            newt "\"Oh hey, I've never seen you around before, the name's Newt. Newt D. Willis!\""
            player "He lends me his hand and I shake it."
            player "\"It's nice to meet you Newt. I'm [player_name].\""
            player "Wow he has such a firm handshake."
            player "After I shook his hand I took a seat next to him and I smell something strange."
            "It smells like someone hasn't showered in weeks."
            "\"Hey uh Newt, do you smell that? It smells like something died in here.\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            trasher_unknown "\"Oh that? That's just my cologne. I like to keep it natural, you know?\""
            "I guess that explains the smell. I don't think I have ever smelled a cologne like that before."
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"You wear cologne? That's a new one.\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            trasher_unknown "\"Yeah, I like to keep it natural. I don't like to use any chemicals or artificial scents.\""
            player "Didn't he just say he uses cologne? Isn't that an artificial scent?"
            player "\"I thought cologne was an artificial scent?\""
            trasher_unknown "\"Oh I just call my natural scent cologne. I don't like to use any chemicals or artificial scents. It is strong enough I might as well consider it a cologne at that point!\""
            player "I guess that makes sense in a way. I mean, if he is allergic to soap, then he can't really use it."
            player"Still though, I don't think I could ever get used to that smell."
            trasher "\"Anyways I realized I haven't even introduced myself, my name's Trasher!\""
            player "\"Wait is that your real name?\""
            trasher "\"Yeah, it's my real name. My parents were really into punk rock and they thought it would be a cool name.\""
            player "I guess that explains the smell. I don't think I have ever met anyone with a name like that before."
            player "Trasher smiles and offers a handshake."
            player "\"Well, it's nice to meet you anyway. I'm [player_name].\""
            trasher "\"Hey Newt, did you end up buying those textbooks I told you about?\""
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"...\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            trasher "\"You know... I told you they were on sale at the bookstore...\""
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"...\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            trasher "\"You know, the ones I told you about last week? The ones we need for class...\""
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"Oh, those textbooks? I forgot to buy them.\""
            

            return

        "Sit in the back row":
            player "I decide to sit in the back row."
            show reiji_neutral at pos4 with dissolve
            show iris_happy at pos2 with dissolve

            jump iris_reiji_class1
            
    


    
   
    show reiji_neutral at pos4 with dissolve
    show iris_happy at pos2 with dissolve

