"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random

def start_game():
    high_score = float('inf') # initializes high score with worst score 'possible'
    print("--------- WELCOME TO THE NUMBER GUESSING GAME ---------")
    
    while True:
        if high_score < float('inf'): # if the user has played
            print("Your high score is {}.".format(high_score))

        winning_number = random.randint(1, 30)
        guesses = 1
    
        while True:
            try:
                player_guess = int(input("Choose a number 1-30. --> "))
                if player_guess > 30 or player_guess < 1:
                    print("The number you guessed is outside of numbers 1-30. Try again!")
                    continue
                elif player_guess < winning_number:
                    print("Your guess is lower than the answer. Try again!")
                    guesses += 1
                    continue
                elif player_guess > winning_number:
                    print("Your guess is higher than the answer. Try again!")
                    guesses += 1
                    continue
                else:
                    if guesses < high_score: # checks if player earned a new high score after winning
                        high_score = guesses
                    print("Woot woot! You got the winning number, {}, in {} guesses.".format(winning_number, guesses))

                play_again = input("Would you like to play again? Y/N: ").lower()
                while play_again != "y" and play_again != "n":
                    print("Please enter 'Y' for yes or 'N' for no.")
                    play_again = input("Would you like to play again? Y/N: ").lower()
                if play_again == "y":
                    print("Awesome, here we go!")
                    break
                else:
                    print("Thank you for playing! Your high score was {} guesses. Exiting game...".format(high_score))
                    return # exits function and ends game
            except ValueError: # catches user input that isn't an integer
                print("Invalid input. Please enter a valid whole number between 1 and 30.")     

start_game()