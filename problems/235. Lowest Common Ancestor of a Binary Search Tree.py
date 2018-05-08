# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        minval = min(p.val,q.val)
        maxval = max(p.val,q.val)

        if root.val>=minval and root.val<=maxval:
            return root

        elif maxval < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        elif minval > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


    def lowestCommonAncestor2(self, root, p, q):

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
