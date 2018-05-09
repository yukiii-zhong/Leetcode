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


    def searchInsert2(self, nums, target):
        i = 0
        j = len(nums)-1

        while j >=i:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid+1
            else:
                j = mid-1

        return i


print(Solution().searchInsert2([1,3,5,6],8))