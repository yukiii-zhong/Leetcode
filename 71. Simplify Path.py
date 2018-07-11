class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        pathList = path.split('/')

        for s in pathList:
            if s =='.' or s == '':
                continue
            elif s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)

        if not stack: return '/'

        res = ''
        for s in stack:
            res += '/'+s
        return res


print(Solution().simplifyPath( "/a/./b/../c/"))
