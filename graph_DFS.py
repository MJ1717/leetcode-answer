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




            