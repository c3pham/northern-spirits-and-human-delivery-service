﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Bunjee", image="magic girl")
    
# The game starts here.
label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show screen main_room
    show screen drag_objects

    "... what should I do today."
    pause
    # This ends the game.
