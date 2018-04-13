# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre1 = dummy1 = ListNode(0)
        pre2 = dummy2 = ListNode(0)
        dummy1.next = l1
        dummy2.next = l2
        while l1 and l2:
            l2.val = l1.val + l2.val
            if l2.val >= 10:
                l2.val -= 10
                if l2.next:
                    l2.next.val +=1
                else:
                    l2.next = ListNode(1)
            l1 = l1.next
            l2 = l2.next
            pre1 = pre1.next
            pre2 = pre2.next
        if l1:
            pre2.next = l1
        l2 = pre2.next
        while l2:
            if l2.val >= 10:
                l2.val -= 10
                if l2.next:
                    l2.next.val +=1
                else:
                    l2.next = ListNode(1)
            l2 = l2.next

        return dummy2.next

