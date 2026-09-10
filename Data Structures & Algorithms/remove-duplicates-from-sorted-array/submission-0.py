class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0

        for i in range(1, len(nums)):
            if nums[p1] != nums[i]:
                p1 += 1
                nums[p1] = nums[i]
        return p1+1