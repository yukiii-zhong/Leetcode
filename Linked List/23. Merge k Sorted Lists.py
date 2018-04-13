# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            newLists = []
            while len(lists)>=2:
                l1 = lists[0]
                l2 = lists[1]
                l3 = self.merge2Lists(l1,l2)
                newLists.append(l3)
                del(lists[0])
                del(lists[0])
            if len(lists) ==1:
                newLists.append(lists[0])
        return self.mergeKLists(newLists)

    def merge2Lists(self,l1,l2):
        pre = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 == None:
            pre.next = l2
        else:
            pre.next = l1
        return dummy.next
