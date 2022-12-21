class Game:
    def __init__(self):
        self.squares = [num for num in range(9)]
        self.game_board = f"""
         {self.squares[0]} | {self.squares[1]} | {self.squares[2]}  
        -----------
         {self.squares[3]} | {self.squares[4]} | {self.squares[5]} 
        -----------
         {self.squares[6]} | {self.squares[7]} | {self.squares[8]} 
        """
        self.status = True

    def take_turn(self, name, symbol):
        while True:
            position = int(input(f"{name}, it's your turn. Input position: "))
            if position in range(9) and position in self.squares:
                self.squares[position] = symbol
                break
            else:
                print("Invalid input. Please try again.")
        self.game_board = f"""
         {self.squares[0]} | {self.squares[1]} | {self.squares[2]}  
        -----------
         {self.squares[3]} | {self.squares[4]} | {self.squares[5]} 
        -----------
         {self.squares[6]} | {self.squares[7]} | {self.squares[8]} 
        """
        print(self.game_board)

    def check_winner(self, symbol):
        # rows
        if self.squares[0] == self.squares[1] == self.squares[2] == symbol or self.squares[3] == self.squares[4] == \
                self.squares[5] == symbol or self.squares[6] == self.squares[7] == self.squares[8] == symbol:
            return True
        # columns
        elif self.squares[0] == self.squares[3] == self.squares[6] == symbol or self.squares[1] == self.squares[4] == \
                self.squares[7] == symbol or self.squares[2] == self.squares[5] == self.squares[8] == symbol:
            return True
        # diagonals
        elif self.squares[0] == self.squares[4] == self.squares[8] == symbol or self.squares[2] == self.squares[4] == \
                self.squares[6] == symbol:
            return True
        else:
            return False
