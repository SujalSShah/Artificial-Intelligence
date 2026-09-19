class QueenChessBoard:
    def __init__(self, size):
        self.size = size
        self.columns = []

    def place_in_next_row(self, column):
        self.columns.append(column)

    def remove_in_current_row(self):
        return self.columns.pop()

    def is_this_column_safe_in_next_row(self, column):
        row = len(self.columns)
        for queen_row, queen_column in enumerate(self.columns):
            # Check same column
            if column == queen_column:
                return False
            # Check diagonal (top-left to bottom-right)
            if queen_column - queen_row == column - row:
                return False
            # Check other diagonal (top-right to bottom-left)
            if queen_column + queen_row == column + row:
                return False
        return True

    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()


def solve_queen(size):
    board = QueenChessBoard(size)
    number_of_solutions = 0
    row = 0
    column = 0

    while True:
        # Try placing queen in current row
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        # If we couldn't place a queen or board is full
        if column == size or row == size:
            if row == size:
                board.display()
                print()
                number_of_solutions += 1
                board.remove_in_current_row()
                row -= 1

            # Backtrack
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:
                break  # All possibilities tried

            row -= 1
            column = prev_column + 1

    print('Number of solutions:', number_of_solutions)


# Main driver
n = int(input('Enter n: '))
solve_queen(n)
