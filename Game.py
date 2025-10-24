import random

class RockPaperScissors:
    def __init__(self, player_score=0, computer_score=0, wins_needed=3):
        self.choices = ['r', 'p', 's']
        self.player_score = player_score    
        self.computer_score = computer_score
        self.wins_needed = wins_needed
        self.rounds_played = []

    def ask_user_choice(self):
        return input("Rock, paper, or scissors? (r/p/s): ")

    # Determine winner
    def determining_winner(self, user_choice, computer_choice):
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            self.rounds_played.append("It's a tie!")
            return

        if (user_choice == 'r' and computer_choice == 's') or \
           (user_choice == 'p' and computer_choice == 'r') or \
           (user_choice == 's' and computer_choice == 'p'):
            self.player_score += 1
            self.rounds_played.append("Player wins!")
        else:
            self.computer_score += 1
            self.rounds_played.append("Computer wins!")

    # play the game
    def playgame(self):
        while self.player_score < self.wins_needed and self.computer_score < self.wins_needed:
            user_choice = self.ask_user_choice()
            computer_choice = random.choice(self.choices)
            self.determining_winner(user_choice, computer_choice)

            print(f"Score - Player: {self.player_score}, Computer: {self.computer_score}")

        if self.player_score == self.wins_needed:
            print("Player wins the game!")
        else:
            print("Computer wins the game!")

        print("Game over!")
        print("Rounds played:")
        for round in self.rounds_played:
            print("-", round)
    
if __name__ == "__main__":
    game = RockPaperScissors()
    game.playgame()
