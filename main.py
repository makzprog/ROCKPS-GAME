from game_logic import Choice, ScoreBoard, GameEgine

if __name__ == "__main__":
    game_1 = GameEgine(Choice(), ScoreBoard())
    game_1.play_game()