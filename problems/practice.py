nums = [3,4,7,9,78]
tgt = 7

class Solution:
    def search(self,nums,tgt):
        i = 0
        j = len(nums)-1

        while i <= j:
            mid = (i+j)//2
            if tgt == nums[mid]:
                return mid
            elif tgt < nums[mid]:
                j = mid-1
            elif tgt > nums[mid]:
                i = mid +1
        return -1

print(Solution().search(nums,1))