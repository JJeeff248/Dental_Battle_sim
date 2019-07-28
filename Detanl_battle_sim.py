# Detal_battle_sim.py
# v0.01

# Modified: 29/07/2019
# Created: 29/07/2019
# By Chris Sa

from error_module import *
from tkinter import *
import time
import sys

root = Tk()
root.title("Dental Battle Sim  | ChrisPy")

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

def title_screen():
    """Display a title screen so that when the user presses any button it switches to a welcome screen"""
    pass
    title_text = """
Hello and welcome to Dental Battle Simulator!
To start press Enter
"""
    title = Label(root, text=title_text)
    title.pack()

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
    canvas = Canvas(root, width = 768, height = 432)
    canvas.pack()
    # title_screen()
    user = username()
    print("Hello {}".format(user))

main()
root.mainloop()
