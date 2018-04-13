# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k ==0 or head == None:
            return head

        # Step1: 1.1 Count length: n
                # 1.2 Make the whole list a circle
        iter = head
        n = 1
        while iter.next:
            n +=1
            iter = iter.next
        iter.next = head

        # Step2: Walk
        iter = head
        for i in range(n-k%n-1):
            iter = iter.next
        temp = iter.next
        iter.next = None
        return temp

