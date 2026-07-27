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