# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        def helper(p,q):
            if not p and not q:
                return True
            if (not p) != (not q):
                return False

            if p.val == q.val:
                return helper(p.left,q.right) and helper(q.left,p.right)
            else:
                return False

        return helper(root.left,root.right)