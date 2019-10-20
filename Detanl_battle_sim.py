# Detal_battle_sim.py

# Modified: 20/10/2019
# Created: 29/07/2019
# By Chris Sa

from error_module import *
from random import randint
import time
import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")


# Dental Battle Sim  | ChrisPy #

def title_screen():
    """Display a title screen and wait for the user to press enter"""

    title = ["    _______   _______ .__   __. .___________. __       _______.___________.     ",
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

    for i in range(len(title)):
        print(title[i])
        
    print("\n\nHello and welcome to Dental Fight Simulator!")
    input("To start press Enter\n")


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
    """List all the options for the user to choose from"""
    color.write("\n=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==", "stdout")
    color.write("\nTo select an option enter the number assigned to it", "stdout")
    color.write("\n1) Start the ", "stdout")
    color.write("tutorial","KEYWORD")
    color.write("\n2) Start the ","stdout")
    color.write("game","KEYWORD")
    color.write("\n3) ","stdout")
    color.write("Quit","KEYWORD")
    color.write("\n=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==\n", "stdout")

    choice = error_check([1,3], "--> ", "ERROR! Please enter a valid number as listed above.", True)
    return choice

def tutorial(user):
    """Teach the user how to play the game"""
    color.write("There is currently no tutorial but there are plans to add one in the near future\n", "console")


def user_attack(user_attacks):
    """Allows the user to choose an attack from a given list"""
    print()
    i = 1
    attacks = []
    for key in sorted(user_attacks):
        print("{}) {}".format(i, key))
        attacks.append(key)
        i += 1
    choice = error_check([1,3], "--> ", "ERROR! Please enter a valid number as listed above.", True)
    attack = attacks[choice - 1]
    return attack


def start(user):
    """Start the game for the user"""
    user_attacks = {"Floss Lasso": [[7,15], "Flossing helps... Flossing too much..."],"Brush Brush": [[4,13], "Brushing helps..."],"See a Dentist": [[16,24], "If you your teeth hurt then you should see a dentist"]}
    enemies = {"Mrs Fizz": ["Acid Spray",[5,20],"The Carbon Dioxied (The thing that makes drinks fizz) in fizzy drinks can cause damage to your teeth because it is acidic"]}

    # Create a list of all the enemies
    enemies_list = []
    for key in sorted(enemies):
        enemies_list.append(key)

    # Select the enemy and it's attack
    enemy = enemies_list[randint(0, len(enemies_list) - 1)]
    enemy_attack = enemies[enemy][0]

    # Set starting HP
    enemy_hp = randint(250, 350)
    user_hp = 300

    while enemy_hp > 0 and user_hp >0:
        attack_choice = user_attack(user_attacks)
        # Calculate damage done to enemy
        damage = user_attacks[attack_choice][0]
        damage_dealt = randint(damage[0], damage[1])
        enemy_hp -= damage_dealt

        # Calculate damage done to user
        damage = enemies[enemy][1]
        enemy_damage_dealt = randint(damage[0], damage[1])
        user_hp -= enemy_damage_dealt

        # Output the stats for the round
        color.write("\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "stdout")
        color.write("\nYou used {}".format(attack_choice), "stdout")
        color.write("\nIt dealt {} damage".format(damage_dealt), "stdout")
        color.write("\n{} now has {}HP".format(enemy, enemy_hp), "stdout")
        color.write("\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "stdout")
        color.write("\n{} used {}".format(enemy, enemy_attack), "stdout")
        color.write("\nIt dealt {} damage".format(enemy_damage_dealt), "stdout")
        color.write("\nYou now have {}HP".format(user_hp), "stdout")
        color.write("\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n", "stdout")

    if user_hp <= 0:
        game_over(user)
    else:
        victory(user)
        

def game_over(user):
    """Allow the user to decide whether they want to try again, return to the main menu or quit after a death"""
    color.write("\nYou ", "stdout")
    color.write("DIED", "COMMENT")
    color.write("\n=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==", "stdout")
    color.write("\nTo select an option enter the number assigned to it", "stdout")
    color.write("\n1) ", "stdout")
    color.write("Menu","KEYWORD")
    color.write("\n2) ","stdout")
    color.write("Try again","KEYWORD")
    color.write("\n3) ","stdout")
    color.write("Quit","KEYWORD")
    color.write("\n=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~=====~==\n", "stdout")

    choice = error_check([1,3], "--> ", "ERROR! Please enter a valid number as listed above.", True)

    if choice == 1:
        start(user)
    elif choice == 3:
        exit_game(user)
    else:
        pass

def victory(user):
    """Congratulate the user"""
    print("Congratulations")


def exit_game(user):
    """Quit the game with"""
    color.write("ChrisPy would like to thank you, ", "TODO")
    color.write("{}".format(user), "KEYWORD")
    color.write(" for taking the time to play my game. I hope to see you again soon", "stdin")
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
    raise SystemExit(0)


def main():
    title_screen()
    user = username()

    while True:
        choice = menu()

        # Check what choice the user inputed then call that function

        if choice == 1 or choice == "tutorial":
            tutorial(user)
        elif choice == 2 or choice == "start":
            start(user)
        else:
            print("Thank you for playing my game. Goodbye")
            exit_game(user)
            


if __name__ == '__main__':
    main()



















