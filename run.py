import random

user_choice = input("Rock, paper, or scissors? (r/p/s): ")

computer_choice = random.choice(['r', 'p', 's'])

if user_choice == computer_choice:
    print("It's a tie!")
    
elif user_choice == 'r':
    if computer_choice == 's':
        print("You win! Rock crushes scissors.")
    else:
        print("You lose! Paper covers rock.")

elif user_choice == 'p':
    if computer_choice == 'r':
        print("You win! Paper covers rock.")
    else:
        print("You lose! Scissors cuts paper.")

elif user_choice == 's':
    if computer_choice == 'p':
        print("You win! Scissors cuts paper.")
    else:
        print("You lose! Rock crushes scissors.")
else:
    print("Invalid choice! Please choose 'r', 'p', or 's'.")