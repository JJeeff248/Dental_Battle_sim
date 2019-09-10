# Detal_battle_sim.py

# Modified: /07/2019
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

def menu():
    """List all the options for the user to do"""
    print("""\n=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==
To select an option enter the letter assigned to it
To Start the tutorial type: T
To Start the game type: S
To Quit the program type: Q
=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==
""")
    # Calling the error module to get a valid input from the user
    choice = error_check(['t','s','q'], "--> ", "ERROR! Please enter a valid letter as listed above.", False)
    return choice

def attacks(user):
    user_attacks = {"Floss Lasso": [[3,7,15], "Flossing helps..."],"Brush Brush": [[4,9,13], "Brushing helps..."],"See a Dentist": [[5,10,14], "If you your teeth hurt then you should see a dentist"]}
    mrs_fizz = {"Dissolve": [[5]],"Spray": [[2]],"Acid Slap": [[4]], "Catch frase i think": "The Carbon Dioxied (The thing that makes them Fizz) in fizzy drinks can cause damage to your teeth because it is acidic"}

def tutorial(user):
    """Teach the user how to play the game"""
    color.write("Welcome to ", "BULLETIN")
    color.write("Dentist Fight Sim \n", "KEYWORD")
    print("When you get into a battle you will have 3 attcaks to chose from, Floss Lasso, Brush Brush and See a Dentist")
    

def start(user):
    """Start the game for the user"""
    pass

def game_over(user):
    """Allow the user to decide whether they want to try again, return to the main menu or quit after a death"""
    print("""\n=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==
To select an option enter the letter assigned to it
To Try Again type: T
To go to the Main menu type: M
To Quit the program type: Q
=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==
""")
    # Calling the error module to get a valid input from the user
    choice = error_check(['t','m','q'], "--> ", "ERROR! Please enter a valid letter as listed above.", False)
    if choice == 't':
        start(user)
    elif choice == 'q':
        exit_game()
    else:
        pass

def exit_game(user):
    print("ChrisPy would like to thank you, {} for taking the time to play my game. I hope to see you again soon".format(user))
    time.sleep(2)
    for i in range (15):
        print("")
        time.sleep(.1)
    end_screen = ["    _______   _______ .__   __. .___________. __       _______.___________.     ",
                  "   |       \ |   ____||  \ |  | |           ||  |     /       |           |     ",
                  "   |  .--.  ||  |__   |   \|  | `---|  |----`|  |    |   (----`---|  |----`     ",
                  "   |  |  |  ||   __|  |  . `  |     |  |     |  |     \   \       |  |          ",
                  "   |  '--'  ||  |____ |  |\   |     |  |     |  | .----)   |      |  |          ",
                  "   |_______/ |_______||__| \__|     |__|     |__| |_______/       |__|          ",
                  "", "",
                  " _______  __    _______  __    __  .___________.        _______. __  .___  ___. ",
                  "|   ____||  |  /  _____||  |  |  | |           |       /       ||  | |   \/   | ",
                  "|  |__   |  | |  |  __  |  |__|  | `---|  |----`      |   (----`|  | |  \  /  | ",
                  "|   __|  |  | |  | |_ | |   __   |     |  |            \   \    |  | |  |\/|  | ",
                  "|  |     |  | |  |__| | |  |  |  |     |  |        .----)   |   |  | |  |  |  | ",
                  "|__|     |__|  \______| |__|  |__|     |__|        |_______/    |__| |__|  |__| "
                  ,""]

    for i in range(len(end_screen)):
        print(end_screen[i])
        time.sleep(0.1)
    
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
        choice = menu()

        # Check what choice the user inputed then call that function

        if choice == 't' or choice == "tutorial":
            tutorial(user)
        elif choice == 's' or choice == "start":
            start(user)
        else:
            print("Thank you for plating my game. Goodbye")
            exit_game(user)
            q = True
    

if __name__ == '__main__':
    main()



















