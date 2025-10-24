import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['r', 'p', 's']
    
    def ask_user_choice(self):
        return input("Rock, paper, or scissors? (r/p/s): ")
    
    def get_computer_choice(self):
        return random.choice(self.choices)
        
    def show_choice(self, choice):
        choice_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        return choice_map.get(choice, 'Invalid choice')
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            show_user = self.show_choice(user_choice)
            show_computer = self.show_choice(computer_choice)
            return f"You chose {show_user}. Computer chose {show_computer}. It's a tie!"
        elif user_choice == 'r':
            if computer_choice == 's':
                show_user = self.show_choice(user_choice)
                show_computer = self.show_choice(computer_choice)
                return f'you choose {show_user} and computer choose {show_computer}. You win! Rock crushes scissors.'
        elif user_choice == 'p':
            if computer_choice == 'r':
                show_user = self.show_choice(user_choice)
                show_computer = self.show_choice(computer_choice)
                return f'you choose {show_user} and computer choose {show_computer}. You win! Paper covers rock.'        
        elif user_choice == 's':
            if computer_choice == 'p':
                show_user = self.show_choice(user_choice)
                show_computer = self.show_choice(computer_choice)
                return f'you choose {show_user} and computer choose {show_computer}. You win! Scissors cuts paper.'
            else:
                show_user = self.show_choice(user_choice)
                show_computer = self.show_choice(computer_choice)
                return f'you choose {show_user} and computer choose {show_computer}. You lose!' 

if __name__ == "__main__":
    game = RockPaperScissors()
    user_choice = game.ask_user_choice()
    computer_choice = game.get_computer_choice()
    result = game.determine_winner(user_choice, computer_choice)
    print(result)
        
