import random

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.options = ["stone", "paper", "scissor"]
        self.user_score = 0
        self.computer_score = 0

    def play(self):
        print("Let's start!")

        for round in range(self.rounds):
            print("Round", round+1)
            user_option = input("Enter your option (stone/paper/scissor): ").lower()
            computer_option = random.choice(self.options)

            if user_option == computer_option:
                print("It's a tie!")
            elif (user_option == "stone" and computer_option == "paper") or \
                 (user_option == "paper" and computer_option == "scissor") or \
                 (user_option == "scissor" and computer_option == "stone"):
                self.computer_score += 1
                print("The computer wins the round!")
            else:
                self.user_score += 1
                print("You win the round!")

        if self.user_score > self.computer_score:
            print("You win the game!")
        elif self.computer_score > self.user_score:
            print("The computer wins the game!")
        else:
            print("It's a tie!")

rounds = int(input("How many rounds do you wish to play? "))
game = Game(rounds)
game.play()