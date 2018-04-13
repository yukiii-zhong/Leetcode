# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        # Step1: Totally copy a list: iter1--> copy1 --> iter2 --> copy2
                # Do not consider random in this step
        iter = head
        while iter:
            copy = RandomListNode(iter.label)
            copy.next = iter.next
            iter.next = copy
            iter = copy.next

        # Step2: From the head, give random pointer to the copies
                # Don't change the linkage, because the pointer is in random
                # You should consider random may be Null
        iter = head
        while iter:
            if iter.random:
                iter.next.random = iter.random.next
            else:
                iter.next.random = None
            iter = iter.next.next

        # Step3: After all the value has been set, make the copy a new list
                # The original list should not be changed
        pre = dummy = RandomListNode(-1)
        iter = head
        while iter:
            pre.next = iter.next
            pre = pre.next
            iter.next = iter.next.next
            iter = iter.next

        return dummy.next


