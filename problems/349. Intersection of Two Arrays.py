class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for n1 in nums1:
            if (n1 in nums2) and n1 not in ans:
                ans.append(n1)

        return ans


    # 使用Python built-in function
    def intersection2(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)



test1= Solution().intersection2([1, 2, 2, 1], [2, 2])
print(test1)