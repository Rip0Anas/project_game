# Created by: [Anas Mohamed]
# Date: 2025-05-22
# Description: This is a simple text-based adventure game
# where the player can choose between two paths: a house or a cave.
# The player can also choose to defend themselves or run away
# The game uses functions to organize the code and make it easier to read
# The game uses the random module to generate random events and outcomes.
# The game uses the time module to create delays between messages
# The game is designed to be simple and easy to understand
# making it suitable for beginners in programming.
import random
import time

score = 0

# This function generates a random enemy name and transformation.
# The function uses the random module,
# to select a random enemy name and transformation from predefined lists.
# The function returns the selected enemy name and transformation as a tuple.
def random_eneimes():
    enemies = ["Muzan", "Pain", "Itachi", "Kisame", "Ghost"]
    transformations = ["snake", "demon", "dust", "spirit"]
    enemy_name = random.choice(enemies)
    transformation = random.choice(transformations)
    return enemy_name, transformation

# This function prints a message and then pauses for 2 seconds before continuing
# This function is used to create a delay between messages in the game.
# This function is called at the beginning of the game to set the scene.
def print_pause(message):
    print(message)
    time.sleep(0.2)

# The funiction is called when the player has completed the game.
# It tells the player his score and thanks him for playing.
# The function also thanks the player for playing and ends the game.
# The function uses the print_pause function to display messages with a delay.
# The function is called at the end of the game to display the final score.
def score_greed():
    print_pause("You have completed the game.")
    print_pause(f"Your score is {score} .")
    print_pause("Thank you for playing this game, See you in another game.")
    print_pause("Game is Ended.")

# if the player want to retry the game
def retry():
    while True:
        print_pause("Do you want to Retry the game?")
        print_pause("Please enter Yes or No.")
        print_pause("1. Yes.")
        print_pause("2. No.")
        choice = input("What is your decision.\n").lower()
        if choice== "yes" :
            print_pause("Excellent!, Restarting the game...")
            play_game()
            break
        elif choice == "no" :
            score_greed()
            exit()
        else:
            print_pause("Please enter Yes or No.")

# Introducing the first scene of the game.
def first_scene():
    print_pause("You find yourself standing in an open field," \
    " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective), magic wand.")

# This function is called to choose between the house and the cave.
def choose():
    while True:
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        choice = input("Please enter 1 or 2.\n")
        enemy_name, transformation = random_eneimes()
        if choice == "1":
            house(enemy_name, transformation)
        elif choice == "2":
            cave(enemy_name, transformation)
        else:
            print_pause("Sorry, please enter 1 or 2.")

# this function is called when the player choose to run away           
def run_away():
    global score
    print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
    print_pause("You have been saved by the magic of the field.")
    score += 60

# This function is callled when the player enters the house.
def house(enemy_name, transformation):
    global score
    while True:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out steps a wicked fairie.")
        print_pause(f"Eep! This is the wicked {enemy_name} that has been terrorizing the village.")
        print_pause("He is blocking the door to the house.")
        print_pause(f"You ask the {enemy_name} to enter the house.")
        print_pause(f"{enemy_name} says, 'Enter if you think you can defeat me!")
        print_pause("You have two choices:")
        print_pause("1. Enter the house.")
        print_pause("2. Run away.")
        print_pause("What would you like to do?")
        choice = input("Please enter 1 or 2.\n")
        if choice == "1":
            print_pause("You enter the house.")
            print_pause(f"{enemy_name} is not happy when he saw you.")
            print_pause(f"He cast a spirit into you and turned you into a {transformation}.")
            print_pause("GAME OVER.")
            score += 50
            retry()

        elif choice == "2":
            print_pause("You run away from the house.")
            print_pause(f"{enemy_name} chases you, but you are too fast for him.")
            run_away()
            print_pause("You escape safely.")
            print_pause("You are now in the field.")
            score += 100
            print_pause(f"You score is {score}.")
            choose()
        else:
            print_pause("Sorry, please enter 1 or 2.")            

# This function is called when the player enters the cave.
def cave(enemy_name, transformation):
    global score
    while True:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be a very large cave.")
        print_pause(f"A wicked {enemy_name} is sitting in the cave.")
        print_pause("He is blocking the entrance.")
        print_pause("You have two choices:")
        print_pause("1. Enter the cave.")
        print_pause("2. Run away.")
        print_pause("What would you like to do?")
        choice = input("Please enter 1 or 2.\n")
        if choice == "1":
            print_pause("You enter the cave.")
            print_pause(f"{enemy_name} is not happy when he saw you.")
            print_pause(f"{enemy_name} said'Huh? You think you can beat me'.")
            print_pause(f"He threw poison at you and turned you into a {transformation}.")
            print_pause("GAME OVER.")
            score += 50
            retry()
            break
        elif choice == "2":
            print_pause("You run away from the cave.")
            print_pause("Orochimaru chases you, but you are too fast for him.")
            print_pause("You escape safely.")
            print_pause("You are now in the field.")
            score += 100
            print_pause(f"Your score is {score}.")
            choose()
        else:
            print_pause("Sorry, please enter 1 or 2.")
            cave(enemy_name, transformation)
            continue

# This function is called when the player has completed the game.
def play_game():
    global score
    score = 0
    first_scene()
    choose()

# This function is called to start the game.  
# It makes the game more organized and easier to read. 
def main():
    play_game()
    
if __name__ == "__main__":
    main()