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



            



.