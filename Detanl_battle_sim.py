# Detal_battle_sim.py

# Modified: 23/10/2019
# Created: 29/07/2019
# By JJeeff248

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
        user = input("\nChoose a 3 character username: ").upper()

        if len(user) == 3:
            valid = True
        else:
            color.write("Please enter a 3 character username", "COMMENT")
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


def user_attack(user_attacks, move_restriction, last_attack):
    """Allows the user to choose an attack from a given list"""
    print()
    i = 1
    attacks = []
    if move_restriction == 2:
        for key in sorted(user_attacks):
            attacks.append(key)
            i += 1
        attacks.remove(last_attack) # Remove the attack that the user can't use for the round
        for i in range(len(attacks)):
            print("{}) {}".format(i+1, attacks[i]))
        choice = error_check([1,2], "--> ", "ERROR! Please enter a valid number as listed above.", True)
        attack = attacks[choice - 1]
    else:
        for key in sorted(user_attacks):
            print("{}) {}".format(i, key))
            attacks.append(key)
            i += 1
        choice = error_check([1,3], "--> ", "ERROR! Please enter a valid number as listed above.", True)
        attack = attacks[choice - 1]
        
    return attack


def start(user):
    """Start the game for the user"""
    user_attacks = {"Floss Lasso": [[3,6], "You should floss once a day. Flossing helps remove old food from inbetween your teath that your tooth brush might not be able to get"],
                    "Brush Brush": [[5,9], "You should brush your teeth twice a day for at least 2 minutes each time. Brushing your teeth is the best way to look after your teeth"],
                    "See a Dentist": [[9, 13], "You should see a dentist if your teeth hurt, it hurts to eat, there is any swelling or you haven't seen them in a while"]}
    enemies = {"Mrs Fizz": ["Acid Spray",[1,6],"The Carbon Dioxide (The thing that makes drinks fizz) in fizzy drinks can cause damage to your teeth because it is acidic which can lead to dental erosion"],
               "JawBreaker": ["Tooth Crush", [8,11], "Jawbreakers contain citric acid which dissolves the enamel on your teeth. The enamel is the protective layer on your teeth, so you don't want to lose it! They can also break your teeth causing lots of pain"],
               "Mr Doug Nut": ["Sugar Assault", [2,7], "Sugar feeds bacteria in your mouth causing plaque (a thin film that coats your teeth), over time the plaque becomes more acidic causing it to eat away at your teeth and form holes"]}
    
    # Create a list of all the enemies
    enemies_list = []
    for key in sorted(enemies):
        enemies_list.append(key)

    # Select the enemy and it's attack
    enemy = enemies_list[randint(0, len(enemies_list) - 1)]
    enemy_attack = enemies[enemy][0]
    damage = enemies[enemy][1]
    enemy_info = enemies[enemy][2]

    # Back story
    color.write("\nYou are minding your own buiseness when you get jumped by ", "stdin")
    color.write(enemy, "COMMENT")
    color.write("! \nThe reason why ", "stdin")
    color.write(enemy, "COMMENT")
    color.write(" is the enemy: \n{}\n\n".format(enemy_info), "stdin")

    # Set starting HP
    enemy_hp = randint(75,125)
    user_hp = 100

    move_restriction = 1
    last_attack = ""

    while enemy_hp > 0 and user_hp > 0:
        attack_choice = user_attack(user_attacks, move_restriction, last_attack)

        # Restrict the number of times a user can use the same move in a row
        if attack_choice == last_attack:
            move_restriction += 1
        else:
            move_restriction = 0

        # Calculate damage done to enemy
        damage = user_attacks[attack_choice][0]
        damage_dealt = randint(damage[0], damage[1])
        enemy_hp -= damage_dealt

        # Calculate damage done to user
        enemy_damage_dealt = randint(damage[0], damage[1])
        user_hp -= enemy_damage_dealt

        # If the hp for the user or enemy is negative set it to 0
        if user_hp < 0 or enemy_hp < 0:
            if enemy_hp <= 0:
                enemy_hp = 0
            else:
                user_hp = 0
        
        # Output the stats for the round
        color.write("\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "stdout")
        color.write("\nYou used {}".format(attack_choice), "stdout")
        color.write("\nIt dealt ", "stdout")
        color.write("{}".format(damage_dealt), "COMMENT")
        color.write(" damage" , "stdout")
        color.write("\n{} now has ".format(enemy), "stdout")
        color.write("{}".format(enemy_hp), "STRING")
        color.write("HP" , "stdout")
        color.write("\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "stdout")
        color.write("\n{} used {}".format(enemy, enemy_attack), "stdout")
        color.write("\nIt dealt ", "stdout")
        color.write("{}".format(enemy_damage_dealt), "COMMENT")
        color.write(" damage" , "stdout")
        color.write("\nYou now have ", "stdout")
        color.write("{}".format(user_hp), "STRING")
        color.write("HP" , "stdout")
        color.write("\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n", "stdout")

        last_attack = attack_choice

        if enemy_hp <= 0:
            victory(user, enemy)
        elif user_hp <= 0:
            game_over(user, enemy)


def game_over(user, enemy):
    """Allow the user to decide whether they want to try again, return to the main menu or quit after a death"""
    color.write("""\n
 _______   _______  _______  _______     ___   .___________. __  
|       \ |   ____||   ____||   ____|   /   \  |           ||  | 
|  .--.  ||  |__   |  |__   |  |__     /  ^  \ `---|  |----`|  | 
|  |  |  ||   __|  |   __|  |   __|   /  /_\  \    |  |     |  | 
|  '--'  ||  |____ |  |     |  |____ /  _____  \   |  |     |__| 
|_______/ |_______||__|     |_______/__/     \__\  |__|     (__)""", "COMMENT")
    color.write("\n\nYou were defeated by ", "stdout")
    color.write("{}".format(enemy), "COMMENT")

    # Print menu of options
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

    if choice == 2:
        start(user)
    elif choice == 3:
        exit_game(user)
    else:
        pass

def victory(user, enemy):
    """Congratulate the user"""
    color.write("""\n
____    ____  __    ______ .___________.  ______   .______     ____    ____  __  
\   \  /   / |  |  /      ||           | /  __  \  |   _  \    \   \  /   / |  | 
 \   \/   /  |  | |  ,----'`---|  |----`|  |  |  | |  |_)  |    \   \/   /  |  | 
  \      /   |  | |  |         |  |     |  |  |  | |      /      \_    _/   |  | 
   \    /    |  | |  `----.    |  |     |  `--'  | |  |\  \----.   |  |     |__| 
    \__/     |__|  \______|    |__|      \______/  | _| `._____|   |__|     (__)""", "STRING")

    color.write("\n\nCongratulations! You have defeated ", "stdout")
    color.write(enemy, "COMMENT")


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


## ----- TODO ----- ##
# * 
