label player_info:
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()  # removes leading/trailing spaces

    if player_name == "":
        $ player_name = "Alex"  # default name if they enter nothing

    "\"My name is [player_name]. It's good to meet you professor Fenton.\""

    fenton "Mix mix swirl mix, [player_name]. What do yer pronouns be? Fenton will remember them for you."

    "Wow, for being a weird little guy he sure is respectful. I guess I should tell him my pronouns."

    menu:
        "What pronouns should we use for you?"
        "He/Him":
            $ player_pronouns = "male"
            $ they = "he"
            $ them = "him"
            $ their = "his"
            $ theirs = "his"

        "She/Her":
            $ player_pronouns = "female"
            $ they = "she"
            $ them = "her"
            $ their = "her"
            $ theirs = "hers"

        "They/Them":
            $ player_pronouns = "non-binary"
            $ they = "they"
            $ them = "them"
            $ their = "their"
            $ theirs = "theirs"

    "I go by [player_pronouns] pronouns. Thank you fo-"
    fenton "Mix mix swirl mix, [player_name]. I will remember that."
    fenton "Now, you should probably get to class. I will see you in the allys someday."
    hide fenton_happy with dissolve
    "W-what does he mean by that? I guess I should get to class now. I don't want to be late on my first day."

    return