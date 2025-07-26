label yomi_class1:
    image classroom = im.Scale("images/scenes/classroom.png", 1920, 1280)
    player"I decide to sit at the back of the class, so I can observe everything without being too close to anyone."
    player"The classroom is filled with first-day chatter. Students are intotroducing themselves, sharing their summer stories, and discussing their expectations for the year."
    player "Except for one girl in the back corner, who seems to be lost in her own world."
    show yomi_happy with dissolve
    player "She's sitting by the window, arms crossed, eyes low. She hasn't spoken a word to anyone since the bell rang."
    player "I feel a little awkward but... maybe I should go say hi?"

    menu:
        "Go sit next to her":
            player "I grab my bag and slip into the empty seat next to her quietly."
            player "She looks up at me, then quickly darts her eyes back down to the ground."
            menu:
                "Introduce myself":
                    player"\"Hi, I'm [player_name], what's your name?"
                    $ affection["yomi"] -= 1
                    yomi "\"...Yomi.\""
                    player"\She speaks softly, barely above a whisper. I can tell she's not used to talking to people."
                    player "I try to make small talk, but she seems uninterested. I guess she's not in the mood for conversation."
                    player "I decide to give her some space and focus on the class."
        
        "Just leave her alone":
            hide yomi_happy with dissolve
            player "I decide to leave her alone. She seems like she wants to be left alone."
            player "I sit back and wait for the class to start."
            player "As I take my seat, I notice a tall, dark-skin man with a big smile on his face walking towards the back of the class and sits next to me."
            show kiota_happy with dissolve
            player "He looks at me, nods his head, and doesn't say a word."
            player "\"Uhhh hey there, I'm [player_name]. Seems like everyone else in class is intro-\""
            kiota_unknown "\"Do you like hamburgers?\""
            player "\"Uhh, yeah I guess?\""
            player "What a weird question to ask on the first day of class. Do I like hamburgers? I mean, who doesn't?"
            kiota_unknown "\"Great! I love hamburgers! I could eat them all day!\""
            player "Well I mean, I guess that's one way to break the ice."
            kiota_unknown "\"But real question is, do you like your hamburgers with or without tomatoes?\""
            menu:
                "With tomatoes":
                    kiota_unknown "\"Ew, really? Tomatoes ruin a perfectly good hamburger! But hey, to each their own, I guess.\""
                    $ affection["kiota"] -= 2
                    player "Oh, well, I guess I should have expected that from him. He seems like the type of guy to take his hamburgers very seriously."
                "Without tomatoes":
                    kiota_unknown "\"Good choice! Tomatoes are the worst part of a hamburger!\""
                    $ affection["kiota"] += 1
                    player "I guess I made the right choice. He seems to be happy with my answer."
                    player "I think we will get along just fine."