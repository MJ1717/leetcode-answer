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

                            
