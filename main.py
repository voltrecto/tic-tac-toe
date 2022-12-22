from game import Game
from player import Player


# Player 1
player1 = Player(name=input("Input Player 1 Name: "), symbol="X")
print(f"Hello {player1.name}. You are Player 1. You are playing {player1.symbol}.")

# Player 2
player2 = Player(name=input("Input Player 2 Name: "), symbol="O")
print(f"Hello {player2.name}. You are Player 2. You are playing {player2.symbol}.")

# Third player object to be used as draw counter.
draw_count = Player(name="Draw", symbol="NA")

players = [player1, player2]
toggle = 0
play_game = True

while play_game:
    game = Game()
    print(game.game_board)
    while game.status:
        player = players[toggle]  # Current player switches every iteration. Starts with player 1.
        if game.check_winner("X"):
            print(f"{player1.name} Wins!")
            player1.score += 1
            game.status = False
        elif game.check_winner("O"):
            print(f"{player2.name} Wins!")
            player2.score += 1
            game.status = False
        elif all(num not in game.squares for num in range(9)):  # Game ends when all squares are filled.
            print("Draw!")
            draw_count.score += 1
            game.status = False
        else:
            game.take_turn(player.name, player.symbol)
            toggle = (toggle + 1) % 2
    print(f"Scores -> {player1.name}: {player1.score} {player2.name}: {player2.score} Draws: {draw_count.score}")
    if input("Do you want to keep playing? (Y/N) ") == "N":
        play_game = False
        print("Thank you for playing!")


