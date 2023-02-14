# This was written by Geoff F. Franke. This is a tic-tac-toe simulator.
import random

class Tic_Tac_Toe:
    
    box = ["0","1","2","3","4","5","6","7","8"]

    def __init__(self) -> None:
        pass

   # This makes the board!
    def show_board(self):
        print(f" {self.box[0]} " + "|" + f" {self.box[1]} " + "|" + f" {self.box[2]} ")
        print("--------------")
        print(f" {self.box[3]} " + "|" + f" {self.box[4]} " + "|" + f" {self.box[5]} ")
        print("--------------")
        print(f" {self.box[6]} " + "|" + f" {self.box[7]} " + "|" + f" {self.box[8]} ")  

   # This starts a game.
    def start_game(self):
        
        print("Welcome to G's tic-tac-toe!")
        choice = input("Enter 1 for computer opponent:\nEnter 2 for human opponent: ")

        #This code is for users against the computer. The counter is that high so that it can be tested well.
        if choice == "1": 
            print("Playing for computer!")
            while True:
                # Shows the board so the player can see it
                self.show_board()
                answer = int(input("Place your X! Choice must be between 0 - 8:  "))
                # If the tile spot is empty then the user can place their X
                if self.box[answer] != "X" and self.box[answer] != "O": 
                    self.box[answer] = "X"
                    # If there's a winner then it would print the message, send the scores, show board, and stop the game
                    if self.who_won():
                        print("We have a winner!")
                        # This sends the scores to the a different file
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"Human 1 won this round!\n")
                        self.show_board()
                        break
                    # If there's no winner then it would print the message, send the scores, show board, and stop the game
                    if self.isFull():
                        print("We have no winner!")
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"No one won this round!\n")
                        self.show_board()
                        break
                # This is the computer opponent    
                while True:     
                    computer_answer = random.randint(0,8)
                    # If the tile spot is empty then the computer can place their O. If it choses the same area it will loop until it finds an empty area 
                    if self.box[computer_answer] != "X" and self.box[computer_answer] != "O":  
                        self.box[computer_answer] = "O"
                        break
                    # If there's a winner then it would print the message, send the scores, show board, and stop the game
                    if self.who_won():
                        print("We have a winner!")
                        # This sends the scores to the a different file
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"Computer won this round!\n")
                        self.show_board()
                        break
                    # If there's no winner then it would print the message, send the scores, show board, and stop the game
                    if self.isFull():
                        print("We have no winner!")
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"No one won this round!\n")
                        self.show_board()
                        break

        # This code is for person vs another person
        else:

            while True:
                self.show_board()

                # This is the first player to choose X
                answer = int(input("Place your X! Choice must be between 0 - 8:  "))

                # If the tile spot is empty then the user can place their X
                if self.box[answer] != "X" and self.box[answer] != "O": 
                    self.box[answer] = "X"
                    # If there's a winner then it would print the message, send the scores, show board, and stop the game
                    if self.who_won():
                        print("We have a winner!")
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"Human 1 won this round!\n")
                        self.show_board()
                        break
                    # If there's no winner then it would print the message, send the scores, show board, and stop the game
                    elif self.isFull():
                        print("We have no winner!")
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"No one won this round!\n")
                        self.show_board()
                        break
             
                self.show_board()
                # This is the second player to choose O
                second_answer = int(input("Place your O! Choice must be between 0 - 8:  "))
                
                # If the tile spot is empty then the user can place their O
                if self.box[second_answer] != "X" and self.box[second_answer] != "O": 
                    self.box[second_answer] = "O"
                    # If there's a winner then it would print the message, send the scores, show board, and stop the game
                    if self.who_won():
                        print("We have a winner :)")
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"Human 2 won this round!\n")
                        self.show_board()
                        break
                    # If there's no winner then it would print the message, send the scores, show board, and stop the game
                    elif self.isFull():
                        print("We have no winner :(")
                        with open("logging_tic_game.txt", "a") as text_file:
                            text_file.write(f"No one won this round!\n")
                        self.show_board()
                        break   
                        
            
    # Uses logic to see if the game is already over and if someon already won                  
    def who_won(self):
        #This checks for the horizontal rows
        if self.box[0] ==  self.box[1] == self.box[2]:
            return True
        if self.box[3] == self.box[4] == self.box[5]:
            return True
        if self.box[6] == self.box[7] == self.box[8]:
            return True
        # This checks for the vertical columns
        if self.box[0] == self.box[3] == self.box[6]:
            return True
        if self.box[1] == self.box[4] == self.box[7]:
            return True
        if self.box[2] == self.box[5] == self.box[8]:
            return True
        # This checks for the diagonals
        if self.box[0] == self.box[4] == self.box[8]:
            return True
        if self.box[2] == self.box[4] == self.box[6]:
            return True
        return False
    
    # Checks to see if the board is full
    def isFull(self):
        for a in self.box:
            if "X" != a and "O" != a:
                return False
        print("It's full")
        return True
