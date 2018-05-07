# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def balanced(root):
            return abs(depth(root.left)-depth(root.right)) <=1


        def depth(root):
            if root is None: return 0
            return 1 + max(depth(root.left),depth(root.right))

        if root is None:
            return True

        if balanced(root):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False