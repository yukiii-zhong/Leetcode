# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Solution1
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode("#")
        dummy.next = head
        node = head
        # node: To be examined
        # Pre: Has been examined
        while node and node.next:
            val = node.val
            while node.next.val == val:
                node = node.next
                pre.next = None
            node = node.next
            if pre.next != None:
                pre = pre.next
            pre.next = node
        return dummy.next

    # Solution2: Recursion
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None or head.next == None:
            return head
        val = head.val
        next = head.next
        if next.val != val:
            head.next = self.deleteDuplicates(next)
            return head
        else:
            while next and next.val == val:
                next = next.next
            return self.deleteDuplicates(next)
