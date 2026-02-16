'''
Python Project: Number Guessing Game
Developed an interactive application where the user attempts to guess a randomly generated number between 1 and 100.
This program provides hints after each guess, tracks the number of attempts, and records the time taken to make the game more engaging. 
'''

import random
import time
#==============================================================================================
print ("Welcome to the Number Guessing Game")

# main game function
def guess_game():
    number_to_guess = random.randint(1,100)
    attempts = 0
    start_time = time.time()

    play_again = "y"

    # main game loop
    while play_again == "y":
        try:
            user_guess = int(input ("\n Enter a number to guess between 1 and 100: "))
        except ValueError:
            print ("Enter a valid integer number")
            continue

        attempts += 1

        # check user guess
        if user_guess < 1 or user_guess > 100:
            print ("Error, Enter a number to guess between 1 and 100")
        elif user_guess > number_to_guess:
            print ("Too High, Try Again.")
        elif user_guess < number_to_guess:
            print ("Too Low, Try Again.")
        else:
            end_time = time.time()
            total_time = int((end_time - start_time))
            print ("Congratulations! you guessed correctly.")
            print (f"Number of attempts: {attempts}")
            print (f"Time Taken: {total_time} seconds")

            # play again method
            while True:
                play_again = input ("\n Click Y to play again or X to exit: ").lower()

                if play_again == "y":
                    number_to_guess = random.randint(1,100)
                    attempts = 0
                    start_time = time.time()
                    break
                elif play_again == "x":
                    print ("Thanks for playing.")
                    break
                else:
                    print ("Error, Please enter Y to play again or X to exit: ")
#==============================================================================================
guess_game()