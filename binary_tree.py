from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        if (p is None and q is None):
            return True
        if (p is None or q is None):
            return False

        queue_p = deque()
        queue_q = deque()

        queue_p.append(p)
        queue_q.append(q)

        while (queue_p and queue_q):
            current_p = queue_p.popleft()
            current_q = queue_q.popleft()

            if (current_p is None and current_q is not None):
                return False

            if (current_p is not None and current_q is None):
                return False

            if (current_p is not None and current_q is not None):

                if (current_p.val != current_q.val):
                    return False
                
                queue_p.append(current_p.left)
                queue_p.append(current_p.right)

                queue_q.append(current_q.left)
                queue_q.append(current_q.right)

        if (len(queue_p) != len(queue_q)):
            return False

        return True


        
        