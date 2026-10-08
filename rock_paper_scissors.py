"""
Workflow of Project:
1- Input from user(Rock,Paper,Scissors)
2-computer choice(computer choice randomly)
3-result printing

cases:
A- Rock:
Rock vs Rock:tie
Rock vs Paper:paper wins
Rock vs Scissors:Rock wins

B- Paper:
Paper vs Paper:tie
Paper vs Rock:Paper wins
Paper vs Scissors:Scissors wins

C- Scissors:
Scissors vs Scissors:tie
Scissors vs Rock:Rock wins
Scissors vs Paper:Scissors wins
"""

import random
item_list = ["Rock","Paper","Scissors"]
user_choice = input("Enter your choice=(Rock,Paper,Scissors): ")
computer_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Match Tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper Wins = Computer Wins")
    elif computer_choice == "Scissors":
        print("Rock Wins = User Wins")

elif user_choice =="Paper":
    if computer_choice == "Rock":
        print("Paper Wins = User Wins")
    elif computer_choice == "Scissors":
        print("Scissors Wins = Computer Wins")

elif user_choice == "Scissors":
    if computer_choice == "Rock":
        print("Rock Wins = Computer Wins")
    elif computer_choice == "Paper":
        print("Scissors Wins = User Wins")
