label player_info:
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()  # removes leading/trailing spaces

    if player_name == "":
        $ player_name = "Alex"  # default name if they enter nothing

    "Nice to meet you, [player_name]. Welcome to the University!"

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

    "Awesome! You have chosen to be [player_pronouns] and you use [they]/[them] pronouns."

    return