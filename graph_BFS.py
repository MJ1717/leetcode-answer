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






        
        