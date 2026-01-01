import random

class Choice:
    def __init__(self, player_choice='x', computer_choice='x'):
        self._player_choice = player_choice
        self._computer_choice = computer_choice
        self._game_choices =  ['r', 'p', 's']
        
    @property
    def player_choice(self):
        return self._player_choice
    
    @property
    def computer_choice(self):
        return self._computer_choice
    
    def ask_player(self):
        self._player_choice = input("Rock, paper, or scissors? (r/p/s): ")
        return self._player_choice
    
    def ask_computer(self):
        self._computer_choice = random.choice(self._game_choices)
        return self._computer_choice    

class ScoreBoard:
    def __init__(self, player_score: int = 0 , computer_score: int = 0):
        self._player_score = player_score
        self._computer_score = computer_score
        self.wins_needed = 3
    
    @property
    def player_score(self):
        return self._player_score

    @player_score.setter
    def player_score(self, value):
        self._player_score = value
        return self._player_score
    
    @property
    def computer_score(self):
        return self._computer_score
    
    @computer_score.setter
    def computer_score(self, value):
        self._computer_score = value
        return self._computer_score
    
class GameEgine:
    def __init__(self, choice: Choice, score: ScoreBoard):
        self.choice = choice
        self.score = score
        self.rounds_played: list = []
    
    def find_winner(self, player_input, computer_input):
        print(f"Player chose: {player_input}")
        print(f"Computer chose: {computer_input}")
        
        if player_input == computer_input:
            self.rounds_played.append("It's a tie!")
        
        if (player_input == 'r' and computer_input == 's') or \
           (player_input == 'p' and computer_input == 'r') or \
           (player_input == 's' and computer_input == 'p'):
            self.score.player_score += 1
            self.rounds_played.append("Player wins!")
        
        else:
            self.score.computer_score += 1
            self.rounds_played.append("Computer wins!")
        
                
    def play_game(self):
        is_valid = self.score.player_score < self.score.wins_needed and self.score.computer_score < self.score.wins_needed
        while is_valid:
            ask_player = self.choice.ask_player()
            ask_computer = self.choice.ask_computer()
            self.find_winner(ask_player, ask_computer)
            
            print(f"Score - Player: {self.score.player_score}, Computer: {self.score.computer_score}")
        
            if self.score.player_score == self.score.wins_needed:
                print("Player wins the game!")
                break
            else:
                print("Computer wins the game!")
               
            
        print("Game over!")
        print("Rounds played:")
            
        for round in self.rounds_played:
            print("-", round)
        

if __name__ == "__main__":
    choice_1 = Choice()
    scores_1 = ScoreBoard()
    game_1 = GameEgine(choice_1, scores_1)
    game_1.play_game()