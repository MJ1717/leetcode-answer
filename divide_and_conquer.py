# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # edge case
        if (len(nums) == 0):
            return None

        def build(left, right):
            
            # base case
            if (left > right):
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(nums) - 1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # # edge case
        # if (head == None):
        #     return None

        # tmp = []

        # current = head

        # while (current != None):
        #     tmp.append([current, current.val])
        #     current = current.next

        # tmp.sort(key=lambda i: i[1])

        # for i in range(len(tmp) - 1):
        #     node, val = tmp[i]

        #     node.next = tmp[i+1][0]
            
        # tmp[-1][0].next = None

        # return tmp[0][0]

        def sort(head):

            if (head is None or head.next is None):
                return head

            slow, fast = head, head.next

            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next

            second_half = slow.next
            slow.next = None

            first = sort(head)
            second = sort(second_half)

            return merge(first, second)

        def merge(node1, node2):

            dummy = ListNode(0)
            current = dummy
            
            while (node1 and node2):
                if (node1.val < node2.val):
                    current.next = node1
                    node1 = node1.next
                else:
                    current.next = node2
                    node2 = node2.next

                current = current.next

            # left over
            if (node1):
                current.next = node1

            if (node2):
                current.next = node2

            return dummy.next

        return sort(head)

            

            
