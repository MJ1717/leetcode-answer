class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_dict(d):
            valid_numbers = ["1","2","3","4","5","6","7","8","9"]

            for key in d.keys():
                if (key not in valid_numbers):
                    return False

            for value in d.values():
                if (value != 1):
                    return False

            return True

        def check_row(row):
            d = {}
            for i in range(9):
                current_number = board[row][i]

                if (current_number == "."):
                    continue

                if (current_number not in d):
                    d[current_number] = 0

                d[current_number] += 1

            return valid_dict(d)

        def check_col(col):
            d = {}
            for i in range(9):
                current_number = board[i][col]

                if (current_number == "."):
                    continue

                if (current_number not in d):
                    d[current_number] = 0

                d[current_number] += 1

            return valid_dict(d)

        def check_sub_box(i, j):
            d = {}

            for x in range(i, i+3):
                for y in range(j, j+3):
                    current_number = board[x][y]

                    if (current_number == "."):
                        continue

                    if (current_number not in d):
                        d[current_number] = 0

                    d[current_number] += 1

            return valid_dict(d)


        # check row
        for i in range(9):
            valid = check_row(i)

            if (valid == False):
                return False

        # check col
        for j in range(9):
            valid = check_col(j)

            if (valid == False):
                return False

        # check sub box
        sub_box = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for (i, j) in sub_box:
            valid = check_sub_box(i, j)

            if (valid == False):
                return False

        return True

        



                
        