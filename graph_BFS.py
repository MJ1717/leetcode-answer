from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        #1. start from index
        #2. see where we can go
        #3. check current is outside
        #4. if we did bfs but still -1.

        def is_empty(i, j):
            result = False
            if (maze[i][j] == "."):
                result = True
                return result
            return result


        def exist_path(lst):
            i = lst[0]
            j = lst[1]

            result = []

            can_left = True
            can_right = True
            can_up = True
            can_down = True

            # left, right
            if (j == 0):
                can_left = False
            if (j == len(maze[0]) - 1):
                can_right = False
            # up, down
            if (i == 0):
                can_up = False
            if (i == len(maze) - 1):
                can_down = False

            if (can_right):
                if (is_empty(i, j+1)):
                    result.append([i, j+1])
            
            if (can_left):
                if (is_empty(i, j-1)):
                    result.append([i, j-1])
            
            if (can_up):
                if (is_empty(i-1, j)):
                    result.append([i-1, j])
            
            if (can_down):
                if (is_empty(i+1, j)):
                    result.append([i+1, j])

            return result

        def is_exit(lst):
            i = lst[0]
            j = lst[1]

            # far left
            if (j == 0):
                return True

            # far right
            if (j == len(maze[0]) - 1):
                return True

            # far up
            if (i == 0):
                return True

            # far down
            if (i == len(maze) - 1):
                return True
            
            return False
        
        def bfs(lst):
            m = len(maze[0])
            n = len(maze)
            visited = [[False] * m for _ in range(n)]

            count = 0 
            queue = deque()
            queue.append((lst, 0))
            visited[lst[0]][lst[1]] = True

            while (queue):
                current_array = queue.popleft()
                current = current_array[0]
                distance = current_array[1]

                connected_list = exist_path(current)
                for neighbor in connected_list:
                    if (visited[neighbor[0]][neighbor[1]] == False):
                        queue.append((neighbor, distance + 1))

                        if (is_exit(neighbor)):
                            distance += 1
                            return distance

                        visited[neighbor[0]][neighbor[1]] = True


            return -1

        return bfs(entrance)




from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        #1. call bfs on (top left)
        #2. get neighbors
           # getting neighbors need helper function
          #  also return neighbors that are inside the matrix
          #  rotten is visited
        #3. if they are not visited, enqueue them into queue.

        def under_bound(i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])):
                return False

            if (grid[i][j] == 0):
                return False

            return True

        def get_neighbors(i, j):
            result = []

            # left
            if (under_bound(i, j-1)):
                result.append([i, j-1])
            
            # right
            if (under_bound(i, j+1)):
                result.append([i, j+1])

            # up
            if (under_bound(i-1, j)):
                result.append([i-1, j])

            # down
            if (under_bound(i+1, j)):
                result.append([i+1, j])       

            return result

        def bfs(i, j):

            while (queue):
                current = queue.popleft()
                i, j, time = current
                grid[i][j] = 2
                neighbors = get_neighbors(i, j)

                for nbr in neighbors:
                    a, b = nbr
                    if (visited[a][b] == False):
                        visited[a][b] = True
                        queue.append([a, b, time + 1])

                if (len(queue) == 0):
                    return time

        def find_rotten():
            result = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if (grid[i][j] == 2):
                        result.append([i,j])
            return result

        def no_fresh_orange():
            result = True
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if (grid[i][j] == 1):
                        return False
            return result

        no_fresh = no_fresh_orange()
        if (no_fresh):
           return 0

        rottens = find_rotten()

        if (len(rottens) == 0):
            return -1

        m = len(grid[0])
        n = len(grid)
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        
        for val in rottens:
            i = val[0]
            j = val[1]
            queue.append([i, j, 0])
            visited[i][j] = True
            grid[i][j] = 2
            
        time = bfs(rottens[0][0], rottens[0][1])
        there_is_fresh = False

        for row in grid:
            if 1 in row:
                there_is_fresh = True
                break

        if (not there_is_fresh):
            return time
        else:
            return -1

                    





        


        






        
        