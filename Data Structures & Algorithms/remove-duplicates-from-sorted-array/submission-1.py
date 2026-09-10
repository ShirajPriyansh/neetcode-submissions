class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
        # p1 = 0

        # for i in range(1, len(nums)):
        #     if nums[p1] != nums[i]:
        #         p1 += 1
        #         nums[p1] = nums[i]
        # return p1+1

        #return len(list(set(nums))) #it won't work because of it doesn't modify the nums in-place and it voilates O(1) 