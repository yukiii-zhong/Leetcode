class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.res = [-1, -1]

        def dfs(i, j):
            if j < i: return

            mid = (i + j) // 2
            if nums[mid] == target:
                if self.res == [-1, -1]:
                    self.res = [mid, mid]
                    dfs(i, mid - 1)
                    dfs(mid + 1, j)
                elif mid < self.res[0]:
                    self.res[0] = mid
                    dfs(i, mid - 1)
                elif mid > self.res[1]:
                    self.res[1] = mid
                    dfs(mid + 1, j)

            elif nums[mid] < target:
                dfs(mid + 1, j)
            elif nums[mid] > target:
                dfs(i, mid - 1)

        dfs(0, len(nums) - 1)
        return self.res

print(Solution().searchRange([5,7,7,8,8,10],5))