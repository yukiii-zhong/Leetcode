# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        p = root.next

        while p != None:
            if p.left:
                p = p.left
                break
            elif p.right:
                p = p.right
                break
            p = p.next

        if root.right:
            root.right.next = p
        if root.left:
            root.left.next = root.right if root.right else p

        self.connect(root.left)
        self.connect(root.right)
