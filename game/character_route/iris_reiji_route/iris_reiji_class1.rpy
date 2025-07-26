#Start of the Iris and Reiji path. Player sits behind Reiji and observes the couple before Reiji notices them

label iris_reiji_class1:
    

    image classroom = im.Scale("images/scenes/classroom.png", 1920, 1280)
    player "You decide to sit behind the couple, taking the seat behind the man" 
    player "After settling down into your seat and grabbing what you need out of your bag, you look up and get a good look at the couple"
    player "A blonde haired woman and a tall dark skinned man who seem to be in their own world"

    show iris_happy at pos2 with dissolve
    show reiji_neutral at pos4 with dissolve

    player "The woman looks completely infatuated and lovestruck with the man. She's sitting away from her own desk and next to the man. Her eyes closed and head pressed against his shoulder, whispering something you can't quite hear to him"
    player "The man is lazing about in his seat like he owns the place, one arm wrapped possessively around the woman with a smirk plastered on his face, nodding along and whispering back to her. The only words you are able to make out are baby girl"
    player "Before long, the mans eyes start to wonder around the classroom, eventually landing on you"
    player "He blows you a kiss and winks"

    #Reiji flirts with the player
    reiji_unknown "\"Hey there cutie, What's your name?\""

    player "Oh..."
    player"Is he flirting with me? His girlfriend is right there"
    
    menu:
        "\"My name is [player_name]\"":
            reiji_unknown "\"[player_name] huh....\""
            "The man looks up and sounds out your name like he is deciding how it tastes before looking back at you with his signature sexy smirk"
            reiji_unknown "\"ha\""
            reiji_unknown "\"Names-\""

    #Iris notices Reiji stopped paying attention to her and is flirting with someone else. Again.

    iris_unknown "\"REIJI!!!!!!!!!\""
    iris_unknown "\"What are you doing?!?!?!?!\""
    if player_pronouns != "female":
        player "You notice the blonde woman staring daggers at you"

    "Reiji turns his head back to the blonde haired woman"
    reiji "\"Calm down baby girl, just messing around. You known I'm only for you\""
    "Reiji lets out a small chuckle. Lifting a leg onto his desk and tilting his head back to you"
    reiji "\"Don't mind my girl Iris here. She's just having her time of the month.\""
    iris "\"Reiji, stop it!!!\""
    reiji "\"Just teasing ya, you know I love how flustered you get when I give someone else attention\""
    "Reiji ruffles Iris's hair and laughs. While Iris crossing her arms and pouts at him, muttering something you can't quite hear clearly"
    "The two of them seem to forget all about you. Slipping right back into their own world as if they never left"
    
    menu:
        "\"You two seem like a cute couple\"":
            if player_pronouns == "female":
                $ affection["iris"] += 1
                $ affection["reiji"] += 1
            else:
                $ affection["reiji"] += 1

            reiji "Flirting back now, are you?"
            
        
        "\"Your girlfriend sounds like a bitch Reiji\"":
            $ affection["iris"] -= 1
            $ affection["reiji"] -= 1
        
            "Reiji goes quite in a instant. His cocky and lovey-dovey playful attitude immediately replaced with a serious and angry tone"
            reiji "No one but me speaks to my girl that way"


        "Leave the lovebirds be":
            "You decide to leave the couple be"
            "They seem very hands-on. To say the least"

        










    
