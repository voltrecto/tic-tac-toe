import random


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def pick_position(self, opponent_symbol, board_state):
        while True:
            position = int(input(f"{self.name}, it's your turn. Input position: "))
            if position in range(9) and position in board_state:
                return position
            else:
                print("Invalid input. Please try again.")


class PlayerAI(Player):
    def pick_position(self, opponent_symbol, board_state):
        print("AI pick its position.")
        # Create a list of all rows, columns and both diagonals, dictionary to save indexes
        board_lists = [[[board_state[0], 0], [board_state[1], 1], [board_state[2], 2]],
                       [[board_state[3], 3], [board_state[4], 4], [board_state[5], 5]],
                       [[board_state[6], 6], [board_state[7], 7], [board_state[8], 8]],
                       [[board_state[0], 0], [board_state[3], 3], [board_state[6], 6]],
                       [[board_state[1], 1], [board_state[4], 4], [board_state[7], 7]],
                       [[board_state[2], 2], [board_state[5], 5], [board_state[8], 8]],
                       [[board_state[0], 0], [board_state[4], 4], [board_state[8], 8]],
                       [[board_state[2], 2], [board_state[4], 4], [board_state[6], 6]]]
        # Try to get a win if possible
        for inner_list in board_lists:
            self_symbol_count = 0
            for item in inner_list:
                if item[0] == self.symbol:
                    self_symbol_count += 1
            if self_symbol_count == 2:
                for item in inner_list:
                    if item[0] != self.symbol and item[0] != opponent_symbol:
                        return item[1]
        # Block if player 1 is about to win
        for inner_list in board_lists:
            opponent_symbol_count = 0
            for item in inner_list:
                if item[0] == opponent_symbol:
                    opponent_symbol_count += 1
            if opponent_symbol_count == 2:
                for item in inner_list:
                    if item[0] != opponent_symbol and item[0] != self.symbol:
                        return item[1]
        # If neither conditions are met, just put a symbol on an available space.
        available_index = [index for index, item in enumerate(board_state) if
                           item != self.symbol and item != opponent_symbol]
        return random.choice(available_index)
