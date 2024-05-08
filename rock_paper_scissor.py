import random

user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input=='q':
        break
    computer_input = random.choice(options)
    print(f"You've chose {user_input} computer has chose {computer_input}")
    if user_input =="rock" and computer_input=="scissors":
        user_wins=user_wins+1
    elif user_input =="paper" and computer_input=="rock":
        user_wins=user_wins+1
    elif user_input =="scissors" and computer_input=="paper":
        user_wins=user_wins+1
    elif user_input==user_wins:
        user_wins=user_wins
        computer_wins=computer_wins
    else:
        computer_wins=computer_wins+1

    print("Your Score = ",user_wins)
    print("Computer Score = ",computer_wins)


if computer_wins>user_wins:
    print("Computer has won!")
elif computer_wins==user_wins:
    print("Match has drawn")
else:
    print("You win!")
