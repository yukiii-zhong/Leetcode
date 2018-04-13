
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr =root
        for length in range(1001):
            if not curr:break
            curr = curr.next
        width,reminder = divmod(length,k)

        ans = []
        curr = root
        for i in range(k):
            head = curr





    def splitListToParts2(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ans = []
        rootLength = self.length(root)
        width, reminder = divmod(rootLength,k)
        curr = root
        for i in range(k):
            head = curr
            for j in range(width + (i<reminder) -1):
                if curr: curr = curr.next
            if curr:
                pre = curr
                curr = curr.next
                pre.next = None
            ans.append(head)
        return ans


    def length(self, head):
        length = 0
        while head:
            length +=1
            head = head.next
        return length


