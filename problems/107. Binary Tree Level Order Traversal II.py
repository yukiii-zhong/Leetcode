# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def dep(root):
            if root == None:
                return 0
            else:
                return 1 + max(dep(root.left), dep(root.right))

        dep = dep(root)
        res = []
        for i in range(dep):
            res.append([])

        def dfs(lev, node):
            if node == None:
                return
            else:
                res[lev] += [node.val]
                dfs(lev - 1, node.left)
                dfs(lev - 1, node.right)

        dfs(dep - 1, root)
        return res
