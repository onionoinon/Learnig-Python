import random

def play(rounds):
    print("Let's start!")
    options = ["stone", "paper", "scissor"]
    user_score = 0
    computer_score = 0

    for round in range(rounds):
        print("Round", round+1)
        user_option = input("Enter your option (stone/paper/scissor): ").lower()
        computer_option = random.choice(options)

        if user_option == computer_option:
            print("It's a tie!")
        elif (user_option == "stone" and computer_option == "paper") or \
             (user_option == "paper" and computer_option == "scissor") or \
             (user_option == "scissor" and computer_option == "stone"):
            computer_score += 1
            print("The computer wins the round!")
        else:
            user_score += 1
            print("You win the round!")

    if user_score > computer_score:
        print("-----------You win the game!-----------")
    elif computer_score > user_score:
        print("-----------The computer wins the game!-----------")
    else:
        print("-----------It's a tie!-----------")

rounds = int(input("How many rounds do you wish to play? "))
play(rounds)
