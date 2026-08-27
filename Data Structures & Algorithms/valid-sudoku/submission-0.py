class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows verification
        # len(board) = 9

        # row verification
        for i in range(9):
            row = [x for x in board[i] if x != "."]
            if len(row) != len(set(row)):
                return False

        # column verification
        for j in range(9):
            column = []
            for i in range(9):
                column.append(board[i][j])
            column = [x for x in column if x != "."]
            if len(column) != len(set(column)):
                return False

        # box verification
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                d = set()
                for i in range(3):
                    for j in range(3):
                        value = board[start_row + i][start_col + j]
                        if value == ".":
                            continue
                        if value in d:
                            return False
                        else:
                            d.add(value)

        return True