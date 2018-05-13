import random

num = random.randint(1,9)
print(num)
guess = 0
count = 0

while guess != "exit":
    guess = input("Guess a Number in between 1-9 or type 'exit' to quit: ").lower()
    count += 1
    try:
        if guess == 'exit':
            break
        elif int(guess) < 1 or int(guess) > 9:
            print ("Please enter a number between 1 to 9!")
            continue
        elif num == int(guess):
            print("You've guessed it exactly right in %s chances!"%count)
            break
        elif num < int(guess):
            if (int(guess)-num) > 2:
                print("Your guess is too high!")
            else:
                print("Your guess is slightly high!")
        elif num > int(guess):
            if (num-int(guess)) > 2:
                print("Your guess is too low!")
            else:
                print("Your guess is slightly low!")
    except ValueError:
        print("Invalid Option, Try Again!")
