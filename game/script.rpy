# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Dargg")
define i = Character("Iris")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dargg happy

    # These display lines of dialogue.

    e "You look tense."

    e "Let me help you with that."

    e "I know who you are"

    show dargg angry
    e "So you don't want my therapy?"

    e "You must suffer."
    # This ends the game.

    hide dargg angry

    image iris_happy = im.Scale("Iris happy.png", 607, 687)

    show iris_happy

    i "Reiji, You're here"

    return
