class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def dfs(i, j, nums):
            if j == i:
                return j
            elif j == i + 1:
                return i if nums[i] > nums[j] else j

            mid = (i + j) // 2
            if nums[mid] > nums[mid + 1]:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    a1 = dfs(i, mid, nums)
                    a2 = dfs(mid + 1, j, nums)
            else:
                a1 = dfs(i, mid, nums)
                a2 = dfs(mid + 1, j, nums)
            return a1 if nums[a1] > nums[a2] else a2

        return dfs(0, len(nums) - 1, nums)