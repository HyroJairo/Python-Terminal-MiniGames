#import random module
import random

# class for rock,paper and scissor game
class Rock_paper_scissor_game:
    
    #instance Varaiable
    user_wins = 0
    computer_wins = 0
  
    #The init method
    def __init__(self):
        pass
    
    def play(self):
        while True:
            options = ["rock", "paper", "scissor"]
        
            #take the input from user
            user_input = input("Type rock/paper/scissor or q to quit: \n").lower()
            if user_input == "q":
                # The results are logged in a text file.  
                if self.user_wins > 0 and self.computer_wins > 0:
                    with open("logging_rps_game.txt", "a") as text_file:
                        text_file.write(f"User won the game {self.user_wins} times while the computer won {self.computer_wins} times\n")
                break
            if user_input not in options:
                continue 
            #initialize the computer choice 
            random_number = random.randint(0,2)
            computer_pick = options[random_number]
            print("Computer picked", computer_pick +".")
        
            #Condition for tie
            if user_input == computer_pick :
                print("Its a tie")
            
            #condition for winning
            elif user_input == "rock" and computer_pick == "scissors":
                print("You won!")
                self.user_wins += 1

            elif user_input == "paper" and computer_pick == "rock":
                print("You won!")
                self.user_wins += 1

            elif user_input == "scissor" and computer_pick == "paper":
                print("You won!")
                self.user_wins += 1

            else:
                print("You Lost!")
                self.computer_wins += 1
        
      
    

