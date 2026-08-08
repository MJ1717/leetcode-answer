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

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        # edge case
        if (root is None):
            return None

        current = None
        parent = None
        found = False
        queue = deque()
        queue.append([root, parent])

        while (queue):
            for _ in range(len(queue)):
                current_node, current_parent = queue.popleft()
                if (current_node.val == key):
                    current = current_node
                    parent = current_parent
                    found = True
                    break

                if (current_node.left is not None):
                    queue.append([current_node.left, current_node])                    
        
                if (current_node.right is not None):
                    queue.append([current_node.right, current_node])

        if (found == False):
            return root

        def how_many_children(node):
            count = 0

            if (node.left is not None):
                count += 1
            if (node.right is not None):
                count += 1

            return count

        count = how_many_children(current)

        # when node has no children
        if (count == 0):

            if (parent is None):
                return None

            if (current is parent.left):
                parent.left = None

            elif (current is parent.right):
                parent.right = None

            return root

        # when node has 1 child
        if (count == 1):
            
            if (parent is None):
                if (current.left is not None):
                    return current.left
                if (current.right is not None):
                    return current.right

            if (current is parent.left):
                if (current.left is not None):
                    child = current.left
                else:
                    child = current.right
                
                parent.left = child

            elif (current is parent.right):
                if (current.left is not None):
                    child = current.left
                else:
                    child = current.right

                parent.right = child

            return root
    
        # when node has 2 child
        if (count == 2):

            if (parent is None):
                current_right = current.right
                current_left = current.left

                if (current_right.left is None):
                    current_right.left = current_left
                    return current_right
                else:
                    last_node = current_left
                    while (True):
                        if (last_node.right is None):
                            break
                        last_node = last_node.right

                    last_node.right = current_right.left
                    current_right.left = current_left

                    return current_right


            if (current is parent.left):
                current_right = current.right
                current_left = current.left

                if (current_right.left is None):
                    parent.left = current_right
                    current_right.left = current_left
                else:
                    last_node = current_left
                    while (True):
                        if (last_node.right is None):
                            break
                        last_node = last_node.right

                    last_node.right = current_right.left
                    current_right.left = current_left
                    parent.left = current_right

            elif (current is parent.right):
                current_right = current.right
                current_left = current.left

                if (current_left.right is None):
                    parent.right = current_left
                    current_left.right = current_right
                else:
                    last_node = current_right
                    while (True):
                        if (last_node.left is None):
                            break
                        last_node = last_node.left

                    last_node.left = current_left.right
                    current_left.right = current_right
                    parent.right = current_left

            return root