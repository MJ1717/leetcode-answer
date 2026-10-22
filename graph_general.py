from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        visited = []

        for i in range(rows):
            row = []

            for j in range(cols):

                if (grid[i][j] == "1"):
                    row.append(0)

                else:
                    row.append(1)

            visited.append(row)

        def get_neighbors(current):
            row, col = current

            neighbors = []

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < rows and 0 <= new_col < cols and visited[new_row][new_col] == 0):
                    neighbors.append((new_row, new_col))

            return neighbors

        def bfs(node):
            queue = deque()
            queue.append(node)

            visited[node[0]][node[1]] = 1

            while (queue):
                current = queue.popleft()

                for neighbor in get_neighbors(current):
                    row, col = neighbor

                    visited[row][col] = 1
                    queue.append(neighbor)

        count = 0
        
        for i in range(rows):
            for j in range(cols):

                if (visited[i][j] == 0):
                    bfs((i, j))
                    count += 1

        return count

                            
from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        visited = [[False] * cols for _ in range(rows)]

        def get_neighbors(row, col):
            neighbors = []
            direction = [(0,1), (0,-1), (1,0), (-1,0)]

            for dr, dc in direction:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == "O" and visited[new_row][new_col] == False):
                    neighbors.append((new_row, new_col))

                
            return neighbors

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited[row][col] = True

            while (queue):
                current_row, current_col = queue.popleft()

                for n_r, n_c in get_neighbors(current_row, current_col):
                    visited[n_r][n_c] = True
                    queue.append((n_r, n_c))

        for row in range(rows):
            for col in range(cols):

                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                    if (board[row][col] == "O" and visited[row][col] == False):
                        bfs(row, col)

        for row in range(rows):
            for col in range(cols):

                if (board[row][col] == "O" and visited[row][col] == False):
                    board[row][col] = "X"


