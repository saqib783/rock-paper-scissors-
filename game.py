import random

user_point = 0
computer_point = 0 
decisionsDict = {1:"rock",2:"paper",3:"scissor"}


while user_point < 3 and computer_point <3:
    userChoice = int(input("Enter 1 for Rock, Enter 2 for Paper, Enter 3 for Scissor"))
    computerChoice = random.randint(1,3)
    print("user chose",userChoice)
    print("computer chose",computerChoice)

    if userChoice == computerChoice:
        print("tie")
    elif(userChoice == 1 and computerChoice == 3) or \
       (userChoice == 2 and computerChoice == 1) or \
        (userChoice == 3 and computerChoice == 2):
        print("user win")
        user_point += 1

    else:
        print("computer win")
        computer_point += 1