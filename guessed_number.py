import random

input("What is your guessed number?")
user_choice = int(input())
available_choice = range(0, 10000)
while not user_choice in available_choice:
    print("Choose another number between 0 and 10000.")
    user_choice = int(input())
computer_choice = random.choice(available_choice)
print(f"You chose {user_choice} and the computer chose {computer_choice}.")
