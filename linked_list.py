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

        

        

  


        