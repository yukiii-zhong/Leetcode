# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        visited = set()

        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ptr2 = self.meetPoint(head)
        if ptr2 == None:
            return None
        ptr1 = head

        while ptr1:
            if ptr1 == ptr2:
                return ptr1
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

    def meetPoint(self,head):
        # Return the meet Point of slow and fast pointers
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        return None