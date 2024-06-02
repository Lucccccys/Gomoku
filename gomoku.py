class Gomoku:
    def __init__(self, size=15):
        # Initialize the board with empty cells
        self.size = size
        # Create a 2D list to represent the board
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        # Set the current player
        self.current_player = 'X'  # Player 'X' starts the game

    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print(' '.join(row))
        print()

    def make_move(self, x, y):
        # Make a move at the given (x, y) position
        if self.board[x][y] == ' ':
            # Place the current player's mark on the board
            self.board[x][y] = self.current_player
            # Check if the move wins the game
            if self.check_win(x, y):
                print(f"Player {self.current_player} wins!")
                return True
            # Switch to the other player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return False
        else:
            print("Invalid move! Try again.")
            return False

    def check_win(self, x, y):
        # Check all directions to see if the current move wins the game
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            # Count consecutive pieces in the positive direction
            count += self.count_in_direction(x, y, dx, dy)
            # Count consecutive pieces in the negative direction
            count += self.count_in_direction(x, y, -dx, -dy)
            if count >= 5:
                return True
        return False

    def count_in_direction(self, x, y, dx, dy):
        # Count consecutive pieces of the same player in a given direction
        count = 0
        player = self.board[x][y]
        i, j = x + dx, y + dy
        while 0 <= i < self.size and 0 <= j < self.size and self.board[i][j] == player:
            count += 1
            i += dx
            j += dy
        return count

if __name__ == "__main__":
    # Prompt the user for the board size
    while True:
        try:
            size = int(input("Enter the board size (an integer greater than 0): "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    game = Gomoku(size)
    game_over = False
    game.print_board()
    
    while not game_over:
        x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
        game_over = game.make_move(x, y)
        game.print_board()
