class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1

        def dfs(i, j, nums, tgt):
            mid = (i + j) // 2

            if i == j:
                if tgt == nums[i]:
                    return i
                else:
                    return -1

            if nums[i] < nums[j]:
                if tgt == nums[mid]:
                    return mid
                elif tgt < nums[mid]:
                    if tgt < nums[i]:
                        return -1
                    else:
                        return dfs(i, mid - 1, nums, tgt)
                elif tgt > nums[mid]:
                    if tgt > nums[j]:
                        return -1
                    else:
                        return dfs(mid + 1, j, nums, tgt)

            elif nums[i] > nums[j]:
                if tgt == nums[mid]:
                    return mid

                if nums[i] <= nums[mid]:
                    if tgt < nums[mid] and tgt >= nums[i]:
                        return dfs(i, mid - 1, nums, tgt)
                    else:
                        return dfs(mid + 1, j, nums, tgt)
                elif nums[i] > nums[mid]:
                    if tgt <= nums[j] and tgt > nums[mid]:
                        return dfs(mid + 1, j, nums, tgt)
                    else:
                        return dfs(i, mid - 1, nums, tgt)

        return dfs(0, len(nums) - 1, nums, target)
