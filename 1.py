from abc import ABC, abstractmethod


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color

class Board:
    board_grid = []
    item_dict = {}

    @classmethod
    def create_items(cls):
        item_dict = {}

        for row in range(8):
            if row == 0:
                item_dict["BR1"] = Rook("black")
                item_dict["BK1"] = Knight("black")
                item_dict["BB1"] = Bishop("black")
                item_dict["BQ1"] = Queen("black")
                item_dict["BKG"] = King("black")
                item_dict["BB2"] = Bishop("black")
                item_dict["BK2"] = Knight("black")
                item_dict["BR2"] = Rook("black")
            elif row == 1:
                for i in range(8):
                    item_dict[f"BP{i+1}"] = Pawn("black")
            elif row == 6:
                for i in range(8):
                    item_dict[f"WP{i+1}"] = Pawn("white")
            elif row == 7:
                item_dict["WR1"] = Rook("white")
                item_dict["WK1"] = Knight("white")
                item_dict["WB1"] = Bishop("white")
                item_dict["WQ1"] = Queen("white")
                item_dict["WKG"] = King("white")
                item_dict["WB2"] = Bishop("white")
                item_dict["WK2"] = Knight("white")
                item_dict["WR2"] = Rook("white")
        return item_dict

    @classmethod
    def create_board(cls, item_dict):
        board = [["   " for _ in range(8)] for _ in range(8)]

        black_order = ["BR1", "BK1", "BB1", "BQ1", "BKG", "BB2", "BK2", "BR2"]
        for col, name in enumerate(black_order):
            board[0][col] = name
        for col in range(8):
            board[1][col] = f"BP{col+1}"

        white_order = ["WR1", "WK1", "WB1", "WQ1", "WKG", "WB2", "WK2", "WR2"]
        for col, name in enumerate(white_order):
            board[7][col] = name
        for col in range(8):
            board[6][col] = f"WP{col+1}"

        return board

    @classmethod
    def setup(cls):
        cls.item_dict = cls.create_items()
        cls.board_grid = cls.create_board(cls.item_dict)

    @classmethod
    def print_board(cls):
        print("\n-------------------------------------------------")
        for row in cls.board_grid:
            print("| ", end="")
            for item in row:
                print(item if item != "   " else "   ", "|", end=" ")
            print("\n-------------------------------------------------")


class Piece(ABC, Board):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def can_move(self, start_row, start_col, end_row, end_col, name):
        pass


class Pawn(Piece):
    def can_move(self, start_row, start_col, end_row, end_col, name):
        possible_pos = []
        direction = -1 if self.color == "white" else 1
        directions = [[direction, 0], [direction, 1], [direction, -1]]

        for dr, dc in directions:
            r, c = start_row + dr, start_col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                possible_pos.append((r, c))

        if (end_row, end_col) in possible_pos:
            Board.board_grid[end_row][end_col] = name
            Board.board_grid[start_row][start_col] = "   "
        else:
            print("Invalid move for Pawn")


class Rook(Piece):
    def can_move(self, start_row, start_col, end_row, end_col, name):
        possible_pos = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dr, dc in directions:
            r, c = start_row + dr, start_col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if Board.board_grid[r][c] == "   ":
                    possible_pos.append((r, c))
                else:
                    if Board.board_grid[r][c][0] != self.color[0].upper():
                        possible_pos.append((r, c))
                    break
                r += dr
                c += dc

        if (end_row, end_col) in possible_pos:
            Board.board_grid[end_row][end_col] = name
            Board.board_grid[start_row][start_col] = "   "
        else:
            print("Invalid move for Rook")


class Knight(Piece):
    def can_move(self, start_row, start_col, end_row, end_col, name):
        possible_pos = []
        moves = [
            [2, 1], [2, -1], [-2, 1], [-2, -1],
            [1, 2], [1, -2], [-1, 2], [-1, -2]
        ]
        for dr, dc in moves:
            r, c = start_row + dr, start_col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                possible_pos.append((r, c))

        if (end_row, end_col) in possible_pos:
            Board.board_grid[end_row][end_col] = name
            Board.board_grid[start_row][start_col] = "   "
        else:
            print("Invalid move for Knight")


class Bishop(Piece):
    def can_move(self, start_row, start_col, end_row, end_col, name):
        possible_pos = []
        directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        for dr, dc in directions:
            r, c = start_row + dr, start_col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if Board.board_grid[r][c] == "   ":
                    possible_pos.append((r, c))
                else:
                    if Board.board_grid[r][c][0] != self.color[0].upper():
                        possible_pos.append((r, c))
                    break
                r += dr
                c += dc

        if (end_row, end_col) in possible_pos:
            Board.board_grid[end_row][end_col] = name
            Board.board_grid[start_row][start_col] = "   "
        else:
            print("Invalid move for Bishop")


class Queen(Piece):
    def can_move(self, start_row, start_col, end_row, end_col, name):
        
        possible_pos = []
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [1, -1], [-1, 1], [-1, -1]
        ]

        for dr, dc in directions:
            r, c = start_row + dr, start_col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if Board.board_grid[r][c] == "   ":
                    possible_pos.append((r, c))
                else:
                    if Board.board_grid[r][c][0] != self.color[0].upper():
                        possible_pos.append((r, c))
                    break
                r += dr
                c += dc

        if (end_row, end_col) in possible_pos:
            Board.board_grid[end_row][end_col] = name
            Board.board_grid[start_row][start_col] = "   "
        else:
            print("Invalid move for Queen")


class King(Piece):
    def can_move(self, start_row, start_col, end_row, end_col, name):
        possible_pos = []
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [1, -1], [-1, 1], [-1, -1]
        ]
        for dr, dc in directions:
            r, c = start_row + dr, start_col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                possible_pos.append((r, c))

        if (end_row, end_col) in possible_pos:
            Board.board_grid[end_row][end_col] = name
            Board.board_grid[start_row][start_col] = "   "
        else:
            print("Invalid move for King")


class Game:
    def __init__(self):
        Board.setup()
        self.players = [Player("Subbu", "white"), Player("Shriya", "black")]
        self.chance = 0  

    def switch_turn(self):
        if self.chance == 0:
            self.chance = 1
        else:
            self.chance = 0

    def play(self):
        while True:
            current_player = self.players[self.chance]
            print(f"{current_player.name}'s Turn ({current_player.color.capitalize()})")
            Board.print_board()

            user_input = input("Enter move (e.g. 6 0 5 0): ").split()
            if len(user_input) != 4:
                print("Invalid input. Please enter exactly 4 numbers.")
                continue

            start_row, start_col, end_row, end_col = map(int, user_input)

            piece_name = Board.board_grid[start_row][start_col]
            if piece_name == "   ":
                print("No piece at that position.")
                continue

        
            piece_color = "white" if piece_name[0] == "W" else "black"
            if piece_color != current_player.color:
                print(f"You cannot move {piece_color} pieces!")
                continue

            piece = Board.item_dict.get(piece_name)
            if piece:
                piece.can_move(start_row, start_col, end_row, end_col, piece_name)
                self.switch_turn() 
            else:
                print("Piece not found.")




game = Game()
game.play()
