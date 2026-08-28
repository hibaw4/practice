class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # len(board) = 9

        # row verification
        for i in range(9):
            row = [x for x in board[i] if x != "."] # we create a list that represents a row that doesn't contain any "." values to detect duplicates correctly
            # to check for duplicates
            if len(row) != len(set(row)):
                return False

        # column verification
        for j in range(9):
            column = [] # because we need to go through all the values of the column
            for i in range(9): # to move vertically
                column.append(board[i][j])
            column = [x for x in column if x != "."] # to remove "." values
            if len(column) != len(set(column)):
                return False

        # box verification
        # to move through boxes
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                d = set()
                # for one box
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