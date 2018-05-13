import random, sys, os

options = ['rock','paper','scissors']
print("Let's Play Rock-Paper-Scissors")
player1 = input("Player: Enter your name: ")
player2 = "Computer"

def game():

    p1_option = input("%s enter your choice: " %player1).lower()
    p2_option = ''.join(random.choices(options))
    print("%s entered his choice as: %s"%(player2,p2_option))

    if p1_option == p2_option:
        print("It's a tie between %s and %s" %(player1, player2))
        replay = input("Would you like to continue (Y/N): ").lower()
        if replay == 'n':
            sys.exit()
        else:
            pass
        return game()
    elif p1_option == 'rock':
        if p2_option == 'scissors':
            print("%s, wins!" %player1)
        else:
            print("%s, wins!" %player2)
    elif p1_option == 'scissors':
        if p2_option == 'paper':
            print("%s, wins!" %player1)
        else:
            print("%s, wins!" %player2)
    elif p1_option == 'paper':
        if p2_option == 'rock':
            print("%s, wins!" %player1)
        else:
            print("%s, wins!" %player2)
    else:
        print("Invalid Entry by %s, Try Again" %player1)
        replay = input("Would you like to continue (Y/N): ").lower()
        if replay == 'n':
            sys.exit()
        else:
            pass
        return game()

game()
os.system("PAUSE")
