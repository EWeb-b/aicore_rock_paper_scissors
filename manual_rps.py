import random

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    print (computer_choice)
    return computer_choice

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors >")
    print("You chose {}".format(user_choice))
    return user_choice

def get_winner(computer_choice, user_choice):
    c, u = computer_choice, user_choice
    if (c == u): print("Draw")
    elif ((c == "Rock" and u == "Scissors") or (c == "Paper" and u == "Rock") or (c == "Scissors" and u == "Paper")):
        print("Computer Wins")
    elif ((u == "Rock" and c == "Scissors") or (u == "Paper" and c == "Rock") or (u == "Scissors" and c == "Paper")):
        print("User Wins")


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()