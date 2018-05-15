import time

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        s = 0
        l = 1

        def helper(slow, fast, nums):

            if fast < len(nums):
                nums[slow + 1], nums[fast] = nums[fast], nums[slow + 1]
                fast = slow +1

            # when fast == len(nums)
            else:
                nums[slow], nums[slow+1] = nums[slow + 1],nums[slow]
                fast = slow +1

            return slow,fast

        while s <len(nums) and l < len(nums):
            if nums[s] <= nums[l]:
                if s<l:
                    s +=2
                else:
                    l +=2
            # nums[s] > nums[l]
            else:
                if l > s:
                    while l < len(nums) and nums[s]> nums[l]:
                        l +=1

                    s,l = helper(s,l,nums)
                else:
                    while s < len(nums) and nums[s] > nums[l]:
                        s +=1
                    l,s = helper(l,s,nums)

    def wiggleSort2(self, nums):

        if len(nums) <=0: return

        for i in range(1,len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i-1]) or \
                    (i % 2 == 0 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]


nums = [4,1,3,2]
time_start = time.time()
Solution().wiggleSort2(nums)
time_end = time.time()

print('time cost',time_end-time_start, 'ms')




