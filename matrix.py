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

        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def traverse_right(row, start, end):
            for i in range(start, end + 1):
                result.append(matrix[row][i])

        def traverse_left(row, start, end):
            for i in range(start, end - 1, -1):
                result.append(matrix[row][i])

        def traverse_down(col, start, end):
            for i in range(start, end + 1):
                result.append(matrix[i][col])
        
        def traverse_up(col, start, end):
            for i in range(start, end - 1, -1):
                result.append(matrix[i][col])

        result = []

        far_up = 0
        far_left = 0
        far_right = len(matrix[0]) - 1
        far_down = len(matrix) - 1

        while (far_left <= far_right and far_up <= far_down):
            traverse_right(far_up, far_left, far_right)
            far_up += 1

            if (far_left > far_right or far_up > far_down):
                break

            traverse_down(far_right, far_up, far_down)
            far_right -= 1

            if (far_left > far_right or far_up > far_down):
                break

            traverse_left(far_down, far_right, far_left)
            far_down -= 1

            if (far_left > far_right or far_up > far_down):
                break

            traverse_up(far_left, far_down, far_up)
            far_left += 1

        return result


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col_len = len(matrix[0])

        # transpose
        for row in range(len(matrix)):
            for col in range(row, col_len):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # left right mirror
        for row in range(len(matrix)):
            for col in (range(col_len // 2)):
                matrix[row][col], matrix[row][(col_len - 1) - col] = matrix[row][(col_len - 1) - col], matrix[row][col]

    

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        # find 0 in first row and first col
        first_row_zero = False
        for j in range(cols):
            if (matrix[0][j] == 0):
                first_row_zero = True
                break

        first_col_zero = False
        for i in range(rows):
            if (matrix[i][0] == 0):
                first_col_zero = True
                break

        # use first row and first col to mark zero
        for i in range(1, rows):
            for j in range(1, cols):

                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # update
        for i in range(1, rows):
            for j in range(1, cols):

                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0

        if (first_row_zero):
            for j in range(cols):
                matrix[0][j] = 0

        if (first_col_zero):
            for i in range(rows):
                matrix[i][0] = 0

        


        