# Detal_battle_sim.py
# v0.03

# Title Page

# Modified: 29/07/2019
# Created: 29/07/2019
# By Chris Sa

from error_module import *
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

    text = """
    _______   _______ .__   __. .___________. __       _______.___________.     
   |       \ |   ____||  \ |  | |           ||  |     /       |           |     
   |  .--.  ||  |__   |   \|  | `---|  |----`|  |    |   (----`---|  |----`     
   |  |  |  ||   __|  |  . `  |     |  |     |  |     \   \       |  |          
   |  '--'  ||  |____ |  |\   |     |  |     |  | .----)   |      |  |          
   |_______/ |_______||__| \__|     |__|     |__| |_______/       |__|          
                                                                                
 _______  __    _______  __    __  .___________.        _______. __  .___  ___. 
|   ____||  |  /  _____||  |  |  | |           |       /       ||  | |   \/   | 
|  |__   |  | |  |  __  |  |__|  | `---|  |----`      |   (----`|  | |  \  /  | 
|   __|  |  | |  | |_ | |   __   |     |  |            \   \    |  | |  |\/|  | 
|  |     |  | |  |__| | |  |  |  |     |  |        .----)   |   |  | |  |  |  | 
|__|     |__|  \______| |__|  |__|     |__|        |_______/    |__| |__|  |__| 
                                                                                


Hello and welcome to Dental Battle Simulator!
To start press Enter
"""
    print(text)
    input("")

def username():
    """Get a 3 Character username from the user for use throughout the game"""
    valid = False
    while valid == False:
        user = input("\nChoose a 3 character user name: ").upper()

        if len(user) == 3:
            valid = True
        else:
            color.write("Please enter a 3 character user name", "COMMENT")
    return user

def exit_game():
    for i in range (15):
        print("")
        time.sleep(.1)
    print("    _______   _______ .__   __. .___________. __       _______.___________.     ")
    time.sleep(.1)
    print("   |       \ |   ____||  \ |  | |           ||  |     /       |           |     ")
    time.sleep(.1)
    print("   |  .--.  ||  |__   |   \|  | `---|  |----`|  |    |   (----`---|  |----`     ")
    time.sleep(.1)
    print("   |  |  |  ||   __|  |  . `  |     |  |     |  |     \   \       |  |          ")
    time.sleep(.1)
    print("   |  '--'  ||  |____ |  |\   |     |  |     |  | .----)   |      |  |        ")
    time.sleep(.1)
    print("   |_______/ |_______||__| \__|     |__|     |__| |_______/       |__|          ")
    time.sleep(.1)
    print("")
    time.sleep(.1)
    print("")
    time.sleep(.1)
    print(" _______  __    _______  __    __  .___________.        _______. __  .___  ___. ")
    time.sleep(.1)
    print("|   ____||  |  /  _____||  |  |  | |           |       /       ||  | |   \/   | ")
    time.sleep(.1)
    print("|  |__   |  | |  |  __  |  |__|  | `---|  |----`      |   (----`|  | |  \  /  | ")
    time.sleep(.1)
    print("|   __|  |  | |  | |_ | |   __   |     |  |            \   \    |  | |  |\/|  | ")
    time.sleep(.1)
    print("|  |     |  | |  |__| | |  |  |  |     |  |        .----)   |   |  | |  |  |  | ")
    time.sleep(.1)
    print("|__|     |__|  \______| |__|  |__|     |__|        |_______/    |__| |__|  |__| ")
    for i in range(30):
        time.sleep(.1)
        print("")
    time.sleep(3)
    print("\n" * 100)
    
    
    

def main():
    title_screen()
    user = username()

    q = False
    
    while q == False:
        choice = input("Choice = ")

        # Check what choice the user inputed then call that function

        if choice == 't' or choice == "tutorial":
            tutorial()
        elif choice == 's' or choice == "start":
            start(user)
        else:
            print("Thank you for plating my game. Goodbye")
            exit_game()
            q = True
    

main()



















