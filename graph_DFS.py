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



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # base case
        if (head == None):
            return None
        
        if (head.next == None):
            return head

        odd_list = head
        even_list = head.next

        odd_head = head
        even_head = head.next

        while (odd_list.next.next != None and even_list.next.next != None):
            # update next list
            odd_list.next = odd_list.next.next
            even_list.next = even_list.next.next

            # move
            odd_list = odd_list.next
            even_list = even_list.next

        # left over
        if (odd_list.next != None and odd_list.next.next != None):
            odd_list.next = odd_list.next.next
            odd_list = odd_list.next

            even_list.next = None

        if (even_list.next != None and even_list.next.next != None):
            even_list.next = even_list.next.next
            even_list = even_list.next

            odd_list.next = None
        
        # add them
        odd_list.next = even_head

        return odd_head

        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node, visited, direction):
            # base case
            if (node is None):
                return 1 + visited
            
            # recursive case
            if (direction == "L"):
                return max(dfs(node.right, 1 + visited, "R"), dfs(node.left, -1, "L"))
            else:
                return max(dfs(node.right, -1, "R"), dfs(node.left, 1 + visited, "L"))

        # edge case
        if (root is None):
            return -1 

        left_max = dfs(root.left, -1, "L")
        right_max = dfs(root.right, -1, "R")

        return max(left_max, right_max)
        


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        # make dict
        graph = [ [] for _ in range(n) ]
        for val in connections:
            first, second = val
            
            graph[first].append([second, 1])
            graph[second].append([first, 0])

        # make visited array, num_change
        visited = [False] * n
        num_change = [0]

        def dfs(node):
            visited[node] = True

            for values in graph[node]:
                next_node, need_reverse = values

                if (visited[next_node] == False):
                    if (need_reverse == 1):
                        num_change[0] += 1
                    dfs(next_node)

        dfs(0)

        return num_change[0]


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        # creating dict, var : target_var, value (var / target_var), visited
        d = {}
        for i in range(len(equations)):
            first, second = equations[i]

            if first not in d:
                d[first] = []
            d[first].append([second, values[i], False])

            if second not in d:
                d[second] = []
            d[second].append([first, 1 / values[i], False])

        def dfs(current, target):
            stack = [[current, 1.0]]

            while (stack):
                current_var, acc = stack.pop()

                if (current_var not in d):
                    continue

                for i in range(len(d[current_var])):
                    next_var, val, visited = d[current_var][i]
                
                    if (next_var == target):
                        return acc * val

                    if (visited == False):
                        d[current_var][i][2] = True
                        stack.append([next_var, acc * val])

            # when we didnt find the path
            return -1.0

        def reset(d):
            for key in d:
                for i in range(len(d[key])):
                    d[key][i][2] = False


        result = []

        for i in range(len(queries)):
            first_var, second_var = queries[i]

            answer = dfs(first_var, second_var)

            result.append(answer)

            reset(d)

        return result

            
        
        
                


        
        






