import random


def rps_game():
    while True:
        choices = ["rock", "paper", "scissors","quit"]

        computer = random.choice(choices[0:3])
        player = None

        # prevent player to answer the word out of choices
        while player not in choices:
            player = input("rock paper or scissors?: ").lower()

        # condition
        if player == "quit":
            break
        elif player == computer:
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Tie")
        elif player == "rock":
            if computer == "paper":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You lose!")
            if computer == "scissors":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You win!")
        elif player == "scissors":
            if computer == "rock":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You lose!")
            if computer == "paper":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You win!")
        elif player == "paper":
            if computer == "scissors":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You lose!")
            if computer == "rock":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You win!")

        # ask the user if they would like to play again or not 
        play_again = input("play again? (yes/no): ").lower()
        # if play_again does not equal yes that means they would like to quit 
        if play_again != "yes":
            break

    print("---Thank you, Bye!---")
