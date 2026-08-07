# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        current = root
        
        while (current is not None):
            # base case
            if (current.val == val):
                return current

            if (val < current.val):
                current = current.left
                continue
            else:
                current = current.right

        return None