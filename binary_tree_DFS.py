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

        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def bfs(node, maxx):
            # base case
            if (node is None):
                return
            
            if (node.val >= maxx):
                result.append(1)
                maxx = node.val

            bfs(node.left, maxx)
            bfs(node.right, maxx)

        maxx = float('-inf')
        result = []

        bfs(root, maxx)

        return len(result)
        
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def bfs(node, remaining):
            # base case
            if (node is None):
                return

            # when there is value
            next_remaining = []

            for val in remaining:
                current_left = val - node.val

                if (current_left == 0):
                    result.append(1)
                
                next_remaining.append(current_left)

            next_remaining.append(target_sum)
            
            bfs(node.left, next_remaining)
            bfs(node.right, next_remaining)

        remaining = [targetSum]
        result = []
        target_sum = targetSum

        bfs(root, remaining)
        return len(result)

