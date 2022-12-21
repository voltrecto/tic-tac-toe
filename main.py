from game import Game
from player import Player


player1 = Player(name=input("Input Player 1 Name: "), symbol="X")
print(f"Hello {player1.name}. You are Player 1. You are playing {player1.symbol}.")
player2 = Player(name=input("Input Player 2 Name: "), symbol="O")
print(f"Hello {player2.name}. You are Player 2. You are playing {player2.symbol}.")
players = [player1, player2]
toggle = 0
game = Game()
print(game.game_board)

while game.status:
    player = players[toggle]  # Current player switches every iteration. Starts with player 1.
    if game.check_winner("X"):
        print("Player 1 Wins!")
        game.status = False
    elif game.check_winner("O"):
        print("Player 2 Wins!")
        game.status = False
    elif all(num not in game.squares for num in range(9)):  # Game ends when all squares are filled.
        print("Draw!")
        game.status = False
    else:
        game.take_turn(player.name, player.symbol)
        toggle = (toggle + 1) % 2

