#Snake Water Gun Game :-
print("\t--> Snake Water Gun Game <--\n")


#Instructions and Logic :-
'''
Instructions____:
    Snake beats water
    Water beats gun
    Gun beats snake
    
    {
        Snake with snake --> Draw
        Water with water --> Draw
        Gun with gun --> Draw 
    }


Game_logic:
    While True:
        computer_input():
        user_input():
        
            User choice > $
            Computer choice > $
            User wins/ Computer win 
            input ___ Do you want to play again or want to quit?
            if play ____ clear everythinga and reatart
            if quit ____ Close()
'''

#Code starts from here :-
import time
import random

#Instructions
instructions = '''Here is the game's instructions...

\tGame Instructions

0 is for Snake
1 is for Water
2 is for Gun


Snake beats water,
Water beats gun,
Gun beats snake,
            <&>
Snake with snake --> Draw
Water with water --> Draw
Gun with gun --> Draw
'''

#Fuctions
def game():
    computer = random.randint(0,2)
    user = int(input("\nEnter 0 for Snake\nEnter 1 for Water\nEnter 2 for Gun\nEnter your choice (0, 1, 2) --> "))
    
    if user == 0 and computer == 0:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nGame Draw!")
    elif user == 0 and computer == 1:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nUser Wins!")
    elif user == 0 and computer == 2:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nComputer Wins!")
    elif user == 1 and computer == 0:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nComputer Wins!")
    elif user == 1 and computer == 1:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nGame Draw!")
    elif user == 1 and computer == 2:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nUser Wins!")
    elif user == 2 and computer == 0:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nUser Wins!")
    elif user == 2 and computer == 1:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nComputer Wins!")
    elif user == 2 and computer == 2:
        print("\nUser enters -->", user, "\nComputer enters -->", computer, "\nGame Draw!")
    elif user > 2 and user < 10:
        print("Number should be 0 to 2:")
    elif user == 111:
        print("Okay dear, let's close the game and get back to the menu...!\n")
        time.sleep(3)
        return start()
    else:
        print("Invalid Command___();\nGame Over!\n")
        time.sleep(2)
        return start()


def start():
    while True:
        asking = input('\nEnter "A" to know about the game\nEnter "P" to play the game\nEnter "Q" to close the game\nEnter your choice: --> ')
        if asking == "P" or asking == "p":
            print("Okay, ready!")
            print("Note: For getting back from game, just enter '111' and game will over and you'll come out of the game!\n\n")
            time.sleep(3)
            print("        Game Starts...        ")
            while True:
                game()
        elif asking == "a" or asking == "A":
            print("\n", instructions)
        elif asking == "Q" or asking == "q":
            sure = input("Are you sure? (Yes/No) --> ")
            if sure == "Yes" or sure == "yes":
                print("Okay, as you wish!\n")
                time.sleep(3)
                exit()
            elif sure == "no" or sure == "No":
                print("Okay, so you want to get back...😅\n")
                time.sleep(2)
            else:
                print("Invalid Command!\n")
                time.sleep(2)
        else:
            print("Invalid Command!\n")
            time.sleep(2)

while True:
    start()