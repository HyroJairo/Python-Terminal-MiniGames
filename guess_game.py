#Author: Jairo Diaz-Ortiz
import random
from check import num

# This is the game to guess a number between 1 and 100
class NumberGuessGame:
    # variables to record a boolean
    outcome = False
    tries = 0
    guesses = 0

    def __init__(self):
        pass
    
    #This method starts the game
    def start(self):
        # Gives you a number of guess to pick a number between 1 and a 100
        print(f"You have {self.guesses} guesses! ")
        print("Pick a number between 1 - 100")
        computer_number = random.randrange(1, 100)

        # This gives you clues as to which if you number is higher or lower than the secret number
        while self.guesses > 0:
            print(f"You have {self.guesses} guesses left")
            guess = num()
            if guess == computer_number:
                self.outcome = True
                break
            elif guess < computer_number:
                print("Too small!")
                self.guesses -= 1
                self.tries += 1
            else:
                print("Too large!")
                self.guesses -= 1
                self.tries += 1
        # These prints out if you lost or won the game
        if self.outcome:
            print("You're correct! Congratulations for winning this game!")  
        else:
            print("You ran out of guesses! That sure sucks :(")

        # This sends the scores to the a different file
        with open("logging.txt", "a") as text_file:
            if self.outcome:
                text_file.write(f"Player won the game with {self.tries} guesses!\n")
            else:
                text_file.write(f"Player lost the game with {self.tries} guesses. :(\n")
    
    #This starts the introduction of the game and lets the user chooose the difficulty of it
    def setup(self):
        print("Welcome to the guessing game!")
        options = ['e', 'm', 'h']

        while(True):
            difficulty = input("Please enter which mode to play in? Easy, Medium, or Hard? You can only enter e, m, or h: ")
            if difficulty in options:
                break
            else:
                print("Wrong input. Please try again")

  
        if difficulty == 'e': self.guesses = 20
        elif difficulty == 'm': self.guesses = 10
        else: self.guesses = 5
        self.start()

      
        
