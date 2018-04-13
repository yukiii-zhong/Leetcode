"""
Given a singly linked list, determine if it is a palindrome.

Follow up:

Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        middle = self.findMiddle(head)
        comp = self.reverse(middle.next)
        curr = head
        while comp:
            if curr.val != comp.val:
                return False
            curr = curr.next
            comp = comp.next
        return True

    def reverse(self, head):
        prev = None
        while head:
            # 用contp储存接下来的Node connection
            contp = head.next
            # 以head为基础，指向prev connections
            head.next = prev
            # 接下来从head开始，都变成了prev
            prev = head
            # 开始下一轮
            head = contp
        return prev

    def findMiddle(self, head):
        # while the length is even number (6), comes to the 3rd node
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


