# Detal_battle_sim.py
# v0.02

# Removed Tkinter until later date

# Modified: 29/07/2019
# Created: 29/07/2019
# By Chris Sa

from error_module import *
from tkinter import *
import time
import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")


# Dental Battle Sim  | ChrisPy #

def title_screen():
    """
    Display a title screen so that when the user presses
    any button it switches to a welcome screen
    """
    
    print("""
Hello and welcome to Dental Battle Simulator!
To start press Enter
""")
    input("")

def username():
    """Get a 3 Character username from the user for use throughout the game"""
    valid = False
    while valid == False:
        user = input("\nChoose a 3 character user name: ")

        if len(user) == 3:
            valid = True
        else:
            color.write("Please enter a 3 character user name", "COMMENT")
    return user


def main():
    title_screen()
    user = username()
    print("Hello {}".format(user))

main()
