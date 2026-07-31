# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if (root == None):
            return 0
        
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)

        return 1 + max(left_max_depth, right_max_depth)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def bfs(node, array):
            # base case
            if (node.left is None and node.right is None):
                array.append(node.val)
                return

            # recursive case
            if (node.left is not None):
                bfs(node.left, array)
            if (node.right is not None):
                bfs(node.right, array)

        first_array = []
        second_array = []

        bfs(root1, first_array)
        bfs(root2, second_array)

        return first_array == second_array

        
        

        
        



