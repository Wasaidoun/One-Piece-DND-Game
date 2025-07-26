label day1_morning:
    play sound "audio/Alarm.mp3" fadein 0.5
    scene black
    with fade
    scene dorm_room
    
    with fade
    "That alarm never gets any easier to wake up to. I guess I should get ready for the day."
    "Wait, what time is it? I should probably check my phone."
    show phone
    with dissolve
    "Oh no! It's already 7:50? Did I really sleep through all my alarms... I am going to be late for my first class! I need to hurry up and get dressed."
    hide phone with dissolve
    "I quickly get dressed and grab my bag. I don't want to be late on my first day."
    "I rush out of my dorm room and head to the university gates. I hope I can make it in time."
    scene school_gate
    with dissolve
    "As I arrive at the university gates, I see a few other students heading to class. I guess I am not the only one running late."
    "I take a deep breath and try to calm down. I can do this. It's just the first day, and I am sure everything will be fine."
    "I walk through the gates and head towards the main building. I can see a few students chatting and laughing, but I am too focused on getting to class on time."
    scene school_hallway
    with dissolve
    "Okay. Hall A. Room 318. I think that's the right place."
    "Or maybe it's Hall B? I should have checked the map before I left."

    menu:
        "Look around for help":
            jump look_around_help
            "Ask someone for help"
        "Try to find it on your own":
            jump find_on_own

label find_on_own:
    "Alright, I should probably ask someone for help. I don't want to be late on my first day and wandering around aimlessly won't help."
    play sound "audio/Bump.mp3" fadein 0.5
    show cappy_happy with dissolve
    unknown "\"Woah there, you took a sharp turn there. You almost bumped into me!\""
    "\"What do you mean almost? I did bump into you!\""
    unknown "\"Oh that was you? I thought it was just the wind. I wasn't really paying attention.\""
    "I look at the guy I bumped into. He is a tall capybara with a muscular build and a friendly smile."
    "He looks familiar, but I can't quite place him."
    "Wait a second..."
    "\"Cappy?\""
    cappy "\"Huh?\""
    # Show cappy thinking
    cappy "\"You know my name? I don't think we've met before.\""
    "\"Seriously? After all that time in South Blue Prep?\""
    "I don't think he remembers me..."
    "To be fair, we were never really close friends, but we did hang out a few times."
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
    "Cappy smiles and scratches his head."
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
    "\"Why are you smoking in the hallway? Isn't that against the rules?\""
    cappy "\"Oh, I don't really care about the rules. I just do what I want.\""
    "I guess that explains why he is skipping class."
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
            #jump skip_class
# Add a label for where they go to skip class
# label skip_class:

label classroom:
    scene black with fade
    
    scene classroom with fade

    "This classroom reminds me of the one I had in South Blue Prep. It has the same old wooden desks and chalkboard."

    "There are a few students already here, chatting and laughing, but not very many seats left. I guess I should find a seat before the class starts."
    "I look around the room and see two empty seats. One in the third row..."
    show newt_happy
    unknown "\"It's been a while since I've seen you man. *Gags*, I thought you would have at least tried to take a shower over the summer break.\""
    hide newt_happy
    show trasher_neutral
    unknown "\"Yeah! My doctor actually told me I am allergic to 99 percent of every soap on the market!\""
    hide trasher_neutral
    show yomi_happy
    unknown "\"...\""
    hide yomi_happy

    "And one in the back row..."
    show reiji_neutral
    unknown "\"Hey baby girl, saved you a seat right here.\""
    hide reiji_neutral
    show iris_happy
    unknown "\"Oh, thank you Reiji. You're so sweet.\""
    hide iris_happy
    
    menu:
        "Sit in the third row":
            "I decide to sit in the third row."
            show newt_happy with dissolve
            newt "\"Oh hey, I've never seen you around before, the name's Newt. Newt D. Willis!\""
            "He lends me his hand and I shake it."
            "\"It's nice to meet you Newt. I'm [player_name].\""
            "Wow he has such a firm handshake."
            "After I shook his hand I took a seat next to him and I smell something strange."
            "It smells like someone hasn't showered in weeks."
            "\"Hey uh Newt, do you smell that? It smells like something died in here.\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            unknown "\"Oh that? That's just my cologne. I like to keep it natural, you know?\""
            "I guess that explains the smell. I don't think I have ever smelled a cologne like that before."
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"You wear cologne? That's a new one.\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            unknown "\"Yeah, I like to keep it natural. I don't like to use any chemicals or artificial scents.\""
            "Didn't he just say he uses cologne? Isn't that an artificial scent?"
            "\"I thought cologne was an artificial scent?\""
            unknown "\"Oh I just call my natural scent cologne. I don't like to use any chemicals or artificial scents. It is strong enough I might as well consider it a cologne at that point!\""
            "I guess that makes sense in a way. I mean, if he is allergic to soap, then he can't really use it."
            "Still though, I don't think I could ever get used to that smell."
            trasher "\"Anyways I realized I haven't even introduced myself, my name's Trasher!\""
            "\"Wait is that your real name?\""
            trasher "\"Yeah, it's my real name. My parents were really into punk rock and they thought it would be a cool name.\""
            "I guess that explains the smell. I don't think I have ever met anyone with a name like that before."
            "Trasher smiles and offers a handshake."
            "\"Well, it's nice to meet you anyway. I'm [player_name].\""
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
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            trasher "\"You forgot to buy them? How could you forget? We talked about it like three times!\""
            "Trasher looks really frustrated. I guess he is really into his studies."
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"Oh, I am sorry. I just got so caught up in the summer break that I forgot about them.\""
            hide newt_happy with dissolve
            show yomi_happy with dissolve
            unknown "\"...\""
            hide yomi_happy with dissolve
            show newt_happy with dissolve
            newt "\"I guess I will have to borrow them from you for now.\""
            hide newt_happy with dissolve
            show trasher_neutral with dissolve
            trasher "\"Yeah, I guess you will. But you better return them to me after class!\""
            hide trasher_neutral with dissolve
            show newt_happy with dissolve
            newt "\"Yeah, I will. I promise.\""
            hide newt_happy with dissolve
            "\"Well at least I made some new friends. I guess this class won't be so bad after all.\""
            "I look around the classroom and see a few more students coming in. I guess the class is about to start."
            return

        "Sit in the back row":
            "I decide to sit in the back row."
            show reiji_neutral with dissolve
            unknown "\"Hey baby, you look like you could use some company. Saved you a seat right next to me.\""
            hide reiji_neutral with dissolve
            show iris_happy with dissolve
            unknown "\"Oh, thank you Reiji-kins. You're so sweet.\""
            "Well that was unexpected. I didn't think I would see a couple in class."
            "They seem really close, like they have been together for a while."
            hide iris_happy with dissolve
            show reiji_neutral with dissolve
            reiji "\"?\""

            
    


    
   
    show reiji_neutral at pos4 with dissolve
    show iris_happy at pos2 with dissolve

