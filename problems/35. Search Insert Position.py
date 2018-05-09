class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1

        while True:
            if j < i:
                return i
            if i == j:
                if nums[i] >= target:
                    return i
                else:
                    return i+1
            else:
                mid = (i+j)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1


print(Solution().searchInsert([1,3,5,6],0))