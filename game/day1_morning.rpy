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

    #Maybe runs into Tommy if look around for help? Just an introduction. Still leading to the classroom or skip
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
            player "Cappy smiles and leads me away from the hallway."
            jump skip_class


# Add a label for where they go to skip class
# label skip_class:

label classroom:
    scene black with fade
    
    scene classroom with fade

    player "This classroom reminds me of the one I had in South Blue Prep. It has the same old wooden desks and chalkboard."

    player "There are a few students already here, chatting and laughing, but not very many seats left. I guess I should find a seat before the class starts."
    player "I look around the room and see three empty seats. One in the third row..."
    show newt_happy
    newt_unknown "\"It's been a while since I've seen you man. *Gags*, I thought you would have at least tried to take a shower over the summer break.\""
    hide newt_happy
    show trasher_neutral
    trasher_unknown "\"Yeah! My doctor actually told me I am allergic to 99 percent of every soap on the market!\""
    hide trasher_neutral
    
    player "One in front of the back row next to the window..."
    show yomi_happy
    yomi_unknown "\"...\""
    hide yomi_happy

    player "And one in the back row on the other side of the room..."
    show reiji_neutral
    reiji_unknown "\"Hey baby girl, saved you a seat right here.\""
    hide reiji_neutral
    show iris_happy
    iris_unknown "\"Oh, thank you. You're so sweet.\""
    hide iris_happy
    
    #Trasher and Newt

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
            "Trasher smiles and offers a handshake."
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
            player "\"Well at least I made some new friends. I guess this class won't be so bad after all.\""
            player "I look around the classroom and see a few more students coming in. It seems the class is about to start."
            return

#Yomi (Use if you want)

        "Sit next to the window":
            player "I decide to take the seat next to the window"
            player "While waiting for class to start you stare out of the window and into the university grounds"
            player "It is a bright and cheerful sunny day"
            player "While staring out the window I notice the reflecting of the lady behind me staring with a mixture of sadness and shyness"
            
            show yomi_happy at pos3 with dissolve
            
            player "As soon as she notices me looking she looks away"
            player "I should probably talk to her or well, at least introduce myself"
            player "She wouldn't have been looking at me if she didn't want to talk, right?"
            player "You turn around to introduce yourself her. Noticing her now staring at her desk"
            player "\"Hi, I'm [player_name]. I noticed you looking at me\""
            yomi_unknown "..."
            yomi "\"I'm Yomi\""
            yomi "..."
            player "\"You don't talk very much, do you?\""
            yomi "..."
            player "Doesn't seem like she wants to talk"
            player "Maybe I could talk about something she likes?"
            player "But I just met her and all I know is her name"
            "You notice her stuff bunny she is clutching against her chest in her right hand. You could ask her about it or you could just leave her be"
            
            menu:
                "\"Your bunny looks really cute in a spooky way. I like the bandages\"":
                    $ affection["yomi"] += 1
                    "You notice Yomi perks up immediately and places her stuffed bunny on the desk."
                    "Her faced changed from sadness to excitment in an instant"
                    yomi "\"She sure is. Her name is Usagi\""
                    yomi "\"I love bunnies they're so cute and fluffy\""
                    yomi "\"Do you like bunnies too?\""
                    player "She seemed to switch instantly"
                    player "\"Um... I guess so\""
                    yomi "\"She is a Nousagi bunny\""
                    yomi "\"Hey, did you know that rabbits teeth never stop growing?\""
                    yomi "\"And they are know to play tricks on each other and humans\""
                    yomi "\"A male bunny is called a buck and a female bunny is called a doe\""
                    yomi "\"They are also crepuscular. Meaning that they are active mostly and dusk and dawn\""
                    yomi "\"Rabbits are herbivors and the don't actually eat carrots. They mostly eat leafy greens and seeds\""
                    player "Oh wow. She is really going off"
                    player "\" That's interest-\""
                    yomi "\"Rabbits also like to make there own homes in the ground. But the Nousagi bunnys like Usagi here make they home in animals abandoned home instead of making their own\""
                    yomi "\"They also really like to play with each other\""
                    yomi "\"Bunnies are prey and are hunted by predators like owls, hawks, eagles, wild dogs, and cats\""
                    player "I can barely get a word in"
                    yomi "\"Oh...\""
                    player "You notice Yomi suddenly tense up and immediately goes back to her quiet, sad, and gloomy state again"
                    yomi "..."
                    player "\"Yomi?\""
                    yomi "..."
                    player "Seems like she doesn't want to speak anymore."
                    player "I should leave her be"

                    player "I look around the classroom and see a few more students coming in. It seems the class is about to start."

                "Ignore her":
                    player "You decide to let it go and not confront her. She seems so shy after all"
                    player "I look around the classroom and see a few more students coming in. It seems the class is about to start."




#Iris and Reiji

        "Sit in the back row":
            player "I decide to take the seat in the back row behind the couple, taking the seat behind the man" 
            player "After settling down into my seat and grabbing what I need out of my bag, I look up and get a good look at the couple"
            player "A blonde haired woman and a tall dark skinned man who seem to be in their own world"

            show iris_happy at pos2 with dissolve
            show reiji_neutral at pos3 with dissolve

            player "The woman looks completely infatuated and lovestruck with the man. She's sitting away from her own desk and next to the man. Her eyes closed and head pressed against his shoulder, whispering something you can't quite hear to him"
            player "The man is lazing about in his seat like he owns the place, one arm wrapped possessively around the woman with a smirk plastered on his face, nodding along and whispering back to her. The only words you are able to make out are baby girl"
            player "Before long, the mans eyes start to wonder around the classroom, eventually landing on me"
            player "He blows me a kiss and winks"

            #Reiji flirts with the player
            
            reiji_unknown "\"Hey there cutie, What's your name?\""

            player "Oh..."
            player "Is he flirting with me? His girlfriend is right there"
    
            menu:
                "\"My name is [player_name]\"":
                    reiji_unknown "\"[player_name] huh....\""
                    "The man looks up and sounds out my name before looking back at me with a smirk"
                    reiji_unknown "\"ha\""
                    reiji_unknown "\"Names-\""

            #Iris notices Reiji stopped paying attention to her and is flirting with someone else. Again.

            iris_unknown "\"REIJI!!!!!!!!!\""
            iris_unknown "\"What are you doing?!?!?!?!\""
            if player_pronouns != "female":
                player "I notice the blonde woman staring daggers at me before turning back to Reiji"

            "Reiji turns his head back to the blonde haired woman"
            reiji "\"Calm down baby girl, just messing around. You known I'm only for you\""
            "Reiji lets out a small chuckle. Lifting a leg onto his desk and tilting his head back to you"
            reiji "\"Don't mind my girl Iris here. She's just having her time of the month.\""
            iris "\"Reiji, stop it!!!\""
            "There is no malice in her tone"
            "Iris turns her head to you and points her index finger at you with an accusatory tone. Her face darkening and playful attitude gone"
            iris "\"And you\""
            iris "\"Stop flirting with my boyfriend. He's mine and mine only\""
            iris "\"My Reiji-kins\""
            player "Calm down lady, he was the one that started flirting with me"
            "Reiji ruffles Iris's hair and laughs."
            reiji "\"Just teasing ya, you know I love how flustered you get when I give someone else attention\""
            "Iris turns back to Reiji, crossing her arms and pouting at him, muttering something I can't quite hear "
            "The two of them seem to forget all about me. Slipping right back into their own world as if they never left"
    
            #The player calls them a cute couple which causes Reiji to offer the player to join them. Iris says she is comfortable with it and Reiji accepts her wishes but convinces her to give it a thought

            menu:
                "\"You two seem like a cute couple\"":
                    if player_pronouns == "female":
                        $ affection["iris"] += 1
                        $ affection["reiji"] += 1
                    else:
                        $ affection["reiji"] += 1

                    "Reiji lets out a small laugh"
                    iris "\"Of course we are\""
                    iris "\"The cutest couple there is\""
                    "Iris flicks her hair back with a sharp hmph. An air of arrogance surrounds her" 
                    iris "\"We outshine everyone. No couple even comes close to us.\""
                    "Iris wraps her arms around Reiji in a soft possessiveness"
                    player "She seems so full of herself"
                    player "\"Right...\""
                    "Iris's face twinges at your comment. Gripping Reiji tighter"
                    iris "\"What's that suppose to mean?\""
                    iris "\"Your just jealous of what Reiji and I have\""
                    player "\"That's not what I said\""
                    reiji "\"Maybe [they] want to join us baby girl?\""
                    iris "\"What?\""
                    iris "\"No\""
                    iris "\"Its just the two of us. We are meant for each other and each other alone\""
                    player "She seems very protective"
                    reiji "\"I'm just saying. We could add some spice into our relationship\""
                    player "\"Reiji looks back to me\""
                    if player_pronouns = "non-binary":
                        reiji "\"And [they] are a cutie. After all\""
                    else:
                        reiji "\"And [they] is a cutie. After all\""
                    "Reiji winks at you again"
                    iris "\"Reiji. You know how I feel about this kind of thing\""
                    reiji "\"I know baby girl, but it could be fun\""
                    reiji "\"I love keeping you all to myself\""
                    reiji "\"But there is so much of me to go around\""
                    iris "\"...\""
                    reiji "\"Cmon babe, don't get your panites in a twist\""
                    reiji "\"Do it for your Reiji-kins\""
                    iris "\"...\""
                    if player_pronouns == "female":
                        iris "\"I'll think about it\""
                        iris "\"And I guess [they] look cute\""
                 
                    else:
                        iris "\"No. No way\""
                        iris "\"Maybe if [they] were a woman\""
                        reiji "\"Cmon Iris. You know you'll always be my number one priority\""
                        iris "\"Fine, I'll think about it. Just for you my Reiji-kins\"" 
                    
                    reiji "\"Personne ne peut te remplacer ma chérie (No one can replace you my darling)\""
                    "Iris's face changes to suprise and she blushes hard at the compilment"
                    iris "\"You learned French?\""
                    reiji "\"I sure did. Leaned it over summer, juste pour toi mon amour (Just for you, my love)\""
                    "Iris blushes even harder. Causing Reiji's smirk to widen"
                    "Reiji lifts Iris's chin up so that she is looking at him. A finger brushing against her lower lip"
                    reiji "\"Like I said Iris. No one, and I mean no one can replace you\""
                    iris "\"Of course no one can replace me, En kaathalan (My love)\""
                    reiji "\"Seems I'm not the only one who learned a new language for my beloved\""
                    iris "\"I only actually learned a few words. Nothing like what you did\""
                    "Reiji gives Iris a kiss on the lips before pulling back"
                    reiji "\"Hey baby girl, its the thought that counts\""
                    reiji "\"And speaking of thought\""
                    reiji "\"I got you a present Iris, but your going to have till lunch\""
                    iris "\"You did?\""
                    reiji "\"And you favourite as well, Gâteau au yaourt\""
                    iris "\"Your the best and most thoughtful boyfriend in the world\""
                    iris "\"I also got you something too. I was going to give it to you now, but I'll wait untill lunch as well\""
                    reiji "\"How thoughtful of you, ma douce (My sweet)\""
                    "Reiji turns around to face you. Causing you a mild, visible suprise"
                    reiji "\"Sorry. I almost forgot you were there\""
                    reiji "\"Its so easy to forget when Iris's beauty and wit blinds me to everyone else but her\""
                    player "\"Uh... That's fine\""
                    player "\"I don't want to intrude on your guys relationship\""
                    reiji "\"Offers still there cutie and I'm only half joking. Don't worry about Iris she'll come around in time if you decide to join us\""
                    reiji "\"Though she has the finally say\""
                    "Iris goes quite again and looks visible uncomfortable as Reiji gives you his offer again"
                    "Reiji turns back to Iris. Whispering something into her ear that you can't catch. Causing Iris to blush hard playfully slap him"
                    "The two of them slip back into their own world again like you wern't even there"
                    player "I should probably leave them be. They seem like they were made for each other"
                    player "Although..."                     
                        
                    player "Eventually I notice that the room fills up completely and the teacher gets up to the board. It seems class is about to start."
                    player "Though I doubt these two lovebirds are going to even be paying attention to the lesson. They seem too busy in their own world"
                    player "And they won't keep their hands off each other"

            
            #Iris being called a bitch is a trigger for her cause of Tommy. 
        
                "\"Your girlfriend seems like a possesive bitch Reiji\"":
                    $ affection["iris"] -= 1
                    $ affection["reiji"] -= 1

                    player "I notice Iris flinch after I call her that"

                    if player_pronouns != "female":
                        player "A second later I feel a hard slap against my cheek"
                        iris "\"How...\""
                        if player_pronouns == "male":
                            iris "\"How dare you. You worthless man!!!\""
                        else:
                            iris "\"How dare you. You worthless person!!!\""
                    else:
                        player "Iris looks like she is visibly holding herself back from attacking me"

                    player "Reiji has gone quiet in a instant. The air around him shifts, his cocky and lovey-dovey playful attitude immediately replaced with a serious and angry tone"
                    player "I notice Iris is on the verge of tears"
        
                    
                    player "Reiji slams a palm on my desk and gets close up to my face"
                    reiji "\"No one but me speaks to my girl that way\""
                    reiji "\"Got it?\""
                    player "I nod quickly. Not expecting his quick 180 in demeanor"
                    reiji "\"Iris is my girl and I won't let anyone say anything bad about her\""
                    reiji "\"And don't ever call her a bitch again\""
                    "Reiji leaves no room for argument"
                    player "I quickly nod again. Unable to even let out a word"
                    player "I notice Reiji's face soften back in a smirk. His demeanor returning to what it was before"
                    reiji "\"Good\""
                    reiji "\"I'll let you off the hook this time\""
                    reiji "\"Now if you excuse me...\""
                    "Reiji guesters over to Iris with his head who is frozen and still on the verge of tears"
                    player "That Reiji guy was intense. I should probably not antagonize him more"
                    player "I try to give them space but its kind of hard not to with them sitting right in front of me"

                    "Reiji wraps his arms possesively around Iris. Leaning down and pressing a kiss against her lips to calm her down"
                    "This seems to snap Iris out of her trace"
                    "Reiji backs away from the kiss and presses Iris's head down to his chest"
                    reiji "\"Iris, Don't worry about [them]. I've got it under control\""
                    "Iris sniffles causing a tear to drop down her cheek which Reiji quickly wipes away"
                    iris "\"Thank you Reiji...\""
                    iris "\"Your the best...\""
                    iris "\"The only man for me\""
                    reiji "\"Of course I am, baby girl\""
                    player "I notice Iris has seemed to return to how she was before"
                    reiji "\"I got you a suprise. But your going to have to wait until lunch\""
                    iris "\"A suprise? Your the most thoughtful boyfriend there is\""
                    reiji "\"And I'll get you your favourite, Gâteau au yaourt\""
                    player "I notice Iris lift her head off of Reiji's chest as she looks up to him smiling on the verge of tears again. But this time happy tears"
                    iris "\"Cake? You know me too well\""
                    iris "\"I don't know what I'd do without you\""

                    player "Eventually I notice that the room fills up completely and the teacher gets up to the board. It seems class is about to start."
                    player "Though I doubt these two lovebirds are going to even be paying attention to the lesson. They seem too busy in their own world"
                    player "And they won't keep their hands off each other"

            #Fast track to next scene

                "Leave the lovebirds be":
                    player "I decide to leave the couple be"
                    player "They seem very hands-on. To say the least"
                    player "Eventually I notice that the room fills up completely and the teacher gets up to the board. It seems class is about to start."
                    player "Though I doubt these two lovebirds are going to even be paying attention to the lesson. They seem too busy in their own world"
                    player "And they won't keep their hands off each other"
                    return





label skip_class:
    scene black with fade
    scene school_track with fade
    show cappy_happy with dissolve
    "All of my preperation for my first day, just to skip the first class."
    "It's only the first class so I won't really be missing much except for introductions really."
    cappy "Here's my favourite hangout spot with my buddies, right under the bleachers."
    "\"Isn't this your first year Cappy?\""
    cappy "\"I've always come here to hangout, way before university. It's peaceful.\""
    "I duck under the bleachers and I'm met with two other guys."
    hide cappy_happy with dissolve
    show kiota_happy with dissolve
    kiota_unknown "\"Oh? who's the new one?\""
    hide kiota_happy with dissolve
    show bo_bo_happy with dissolve
    bo_bo_unknown "\"Oooh oooh! Cappy you've already made a new friend?\""
    hide bo_bo_happy with dissolve
    show cappy_happy with dissolve
    cappy "\"Yep! This is the newbie I met, [their] name is [player_name]."
    hide cappy_happy
    show kiota_happy 
    kiota "\"Heya [player_name], my name's Kiota! But you can call me Kiota if you'd like.\""
    player "\"Didn't you just tell me your name is Kiota...?\""
    kiota "\"Huh I did? Oh well, the name's Kiota!\""
    "\"I'm just gonna pretend he only introduced himself once\""
    hide kiota_happy
    show bo_bo_happy
    bo_bo "\"Well if it isn't [player_name], what a pleasure it is to meet you. You can call me Bo Bo."

    


    
   
    show reiji_neutral at pos4 with dissolve
    show iris_happy at pos2 with dissolve

