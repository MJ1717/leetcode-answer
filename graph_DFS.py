class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        #1. make visited array, start with false
        #2. go room, and take key
        #3. go to room that we have key
        #4. check visited array, if theres false, then return false



        visited = [False] * len(rooms)

        def dfs(index):
            # when room is visited already
            if (visited[index] == True):
                return

            # mark visited, and get keys
            visited[index] = True
            key_array = rooms[index]

            for key in key_array:
                dfs(key)
            
            return

        dfs(0)
        
        cannot_traverse = False in visited

        return not cannot_traverse


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #1. need visited array to track provinces
        #2. need provinces array to track connected provinces, ex) [ [quebec ontario], [BC saskatchewan]]
        #3. call dfs at first province. each visited province,
         #   update visited array, and add it to connected province
        #4. call dfs again until every province is visited = all values in visited array is true
        #5. return the size of connected province array

        visited = [False] * len(isConnected)
        connected = []

        def neighbors(index):
            result = []
            for i, val in enumerate(isConnected[index]):
                if (val == 1):
                    result.append(i)
            return result
                
        def bfs(index, count):
            visited[index] = True
            connected[count].append(index)
            nbrs = neighbors(index)

            for neighbor_index in nbrs:
                if (visited[neighbor_index] == False):
                    bfs(neighbor_index, count)
                
        def all_visited():
            if (False in visited):
                return False
            return True
        
        count = 0
        index = 0
        while (not all_visited()):
            index = visited.index(False)
            connected.append([])

            bfs(index, count)

            count += 1

        return len(connected)






