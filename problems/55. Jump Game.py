class Solution(object):
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        elif n == 1:
            return True

        judge = [False for _ in range(n)]

        judge[-1] = True

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n - 1:
                judge[i] = True
            for t in range(1, nums[i] + 1):
                if judge[i + t] == True:
                    judge[i] = True
                    break

        return judge[0]

