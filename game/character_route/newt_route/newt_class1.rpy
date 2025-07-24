label newt_class1:
    image classroom = im.Scale("images/scenes/classroom.png", 1920, 1280)
    "I decide to sit in the front row, so I can see the board better. Next to me is a small desk that can barely fit this large mans body."
    show newt_happy with dissolve
    "As soon as I sat down, he just darts his eyes to me and smiles."
    newt_unknown "\"Hey hey hey, I haven't seen you around. I'm Newt! It's a pleasure to meet you!\""
            
    menu:
        "\"Wow uhh, do you always sit this close to people?\"":
            "I ask him if he always sits this close to people."
            newt "\"Oh, sorry about that. I am a pretty big guy so I don't mean to bother you at all. Sitting at this desk is already hard as it is.\""
            "I guess he is just a friendly guy."
            $ affection["newt"] -= 1

        "\"Yeah, I guess you are just a friendly guy. My name is [player_name]\"":
            newt "\"Nice to meet you [player_name]!\""
            $ affection["newt"] += 1
            "I guess he is just a friendly guy."

    "He just starts to dart his head around the room, looking at all the other students."
    newt "\"So, have you seen a man named Cappy? I've been looking for him all day! He said he will be here but I haven't seen him.\""
    "\"Yeah, I just saw him at the school gate. He said he was going to skip class and hang out.\""
    newt "\"Oh Cappy... of course he is skipping the first lecture of the year why wouldn't he. You met him earlier today?\""
    "I nod my head."
    newt "\"Oh, I see. Well, I guess I will have to catch up with him later. He is a good guy, but he can be a bit of a slacker sometimes.\""
            

            
    return
