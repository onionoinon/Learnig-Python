import random

rounds=int(input("How many rounds do you wish to play? "))
print("OK! Lets start!")

options=["stone","paper","scissor"]

user_score=0
computer_score=0

for round in range(rounds):
  print("Round", round+1)
  user_option=input("Enter your option (stone/paper/scissor):").lower
  computer_option=random.choice(options)

  if user_option == computer_option:
        print("Its a tie !")
  elif (user_option == "rock" and computer_option == "paper") or \
       (user_option == "paper" and computer_option == "scissors") or \
        (user_option == "scissors" and computer_option == "rock"):
        computer_score+=1
  else:
      user_score+=1

if (user_score>computer_score):
  print("The user wins!!")
elif (computer_score>user_score):
  print("The computer wins!!")
else:
  print("Its a tie!!")