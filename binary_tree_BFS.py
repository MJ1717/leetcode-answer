# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        #1. if root is empty, return []
        #2. we want to see the most right node, in each level

        if (root == None):
            return []

        queue = [root]
        result = []
    
        while (queue):
            for _ in range(len(queue)):
                current = queue.pop(0)
                
                if (current.left != None):
                    queue.append(current.left)
                
                if (current.right != None):
                    queue.append(current.right)
            
            result.append(current.val)

        return result



from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        result = []
        queue = deque()
        queue.append(root)

        while(queue):
            level_node_num = len(queue)
            level_sum = 0

            for _ in range(level_node_num):
                current = queue.popleft()
                level_sum += current.val

                if (current.left is not None):
                    queue.append(current.left)

                if (current.right is not None):
                    queue.append(current.right)

            result.append(level_sum)

        maxx = float('-inf')
        maxx_index = -1

        for i in range(len(result)):
            if (result[i] > maxx):
                maxx = result[i]
                maxx_index = i

        #maxx_val = max(result)
        #maxx_index = result.index(maxx_val)
        return maxx_index + 1
