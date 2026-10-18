# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        array = []
        current = head
        array.append(current)

        while (current.next != None):
            current = current.next
            array.append(current)

        if (len(array) == 1):
            return None
        if (len(array) == 2):
            array[0].next = None
            return array[0]

        modify_index = (len(array) // 2) - 1
        array[modify_index].next = array[modify_index + 2]

        return head



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # edge case
        if (head is None):
            return None
        if (head.next is None):
            return head

        prev = None
        current = head
        next_element = head.next
        
        while (True):
            # save next element
            next_element = current.next

            # save current
            tmp_prev = current

            # update
            current.next = prev
            prev = tmp_prev     

            if (next_element is None):
                return current

            current = next_element



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # edge case
        if (head is None):
            return 0

        array = []
        current = head
        array.append(current.val)

        # update array
        while (current.next is not None):
            current = current.next
            array.append(current.val)

        front = 0
        back = len(array) - 1
        maxx = -1

        while (front < back):
            current_sum = array[front] + array[back]
            maxx = max(maxx, current_sum)

            front += 1
            back -= 1
            
        return maxx



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None):
            return False

        slow = head
        fast = head

        while (fast.next is not None and fast.next.next is not None):            
            slow = slow.next
            fast = fast.next.next

            if (fast is slow):
                return True

        return False
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        result = []

        current_1 = l1
        current_2 = l2
        prev = 0

        while (current_1 is not None and current_2 is not None):
            val1 = current_1.val
            val2 = current_2.val

            summ = val1 + val2 + prev
            result.append(ListNode(summ % 10))

            if (summ >= 10):
                prev = 1
            else:
                prev = 0

            current_1 = current_1.next
            current_2 = current_2.next

        # left over l1
        while (current_1 is not None):
            val1 = current_1.val

            summ = val1 + prev
            result.append(ListNode(summ % 10))

            if (summ >= 10):
                prev = 1
            else:
                prev = 0

            current_1 = current_1.next

        # left over l2
        while (current_2 is not None):
            val2 = current_2.val

            summ = val2 + prev
            result.append(ListNode(summ % 10))

            if (summ >= 10):
                prev = 1
            else:
                prev = 0

            current_2 = current_2.next

        if (prev == 1):
            result.append(ListNode(1))

        for i in range(len(result) - 1):
            current = result[i]
            current.next = result[i + 1]

        return result[0]
            




        