#Authors: Jairo Diaz-Ortiz(guessing game), Pavithra Venkatesh(rock paaper scissors game), Geoffrey Franke (tic-tac-toe game)
import guess_game
import rps_game
import tic_tac_toe

# Simple menu which introduces three games for the user to pick or they can quit the menu
while True:
    answer = input("Welcome to the gaming portal!\n\
    Enter 1 for the guessing game or\n\
    Enter 2 for the rock paper scissors game or\n\
    Enter 3 for the tic-tac-toe game or\n\
    Enter 0 to quit the portal:  ")

    if answer == "1":
        guessing = guess_game.NumberGuessGame()
        guessing.setup()

    elif answer == "2":
        rock = rps_game.Rock_paper_scissor_game()
        rock.play()
        
    elif answer == "3":
        tick = tic_tac_toe.Tic_Tac_Toe()
        tick.start_game()
     
    elif answer == "0":
        break

print("Thanks for playing!")