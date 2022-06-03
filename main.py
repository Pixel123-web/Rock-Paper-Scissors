import random

while True:
    move_bank = ["R", "P", "S"]

    player_move = input("enter R for Rock, P for Paper or S for Scissors: ")
    computer_move = random.choice(move_bank)

    if player_move != "R" or "P" or "S":
        print("Invalid input, try again")
    
    print(f"Player {player_move} : Computer {computer_move}. \n")
    
    if player_move == computer_move:
        print("Oh shooks, it's a draw. Play again? ")
    elif player_move == "R":
        if computer_move == "P":
            print("Paper covers rock. You lose!")
        else:
            print("Rock smashes scissors. You win!")
    elif player_move == "P":
        if computer_move == "R":
            print("Paper covers rock. You win!")
        else: 
            print("Scissors cuts paper. You lose!")
    elif player_move == "S":
        if computer_move == "R":
            print("Rock smashes scissors. You lose!")
        else:
            print("Scissors cut paper. You win!")
    
    keep_playing = input("do you want to keep playing? (yes or no): ")
    if keep_playing.lower() != "yes":
        break