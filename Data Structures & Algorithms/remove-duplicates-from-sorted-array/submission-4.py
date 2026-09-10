class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0

        for i in range(1, len(nums)):
            if nums[p1] != nums[i]:
                p1 += 1
                nums[p1] = nums[i]
        return p1+1


        # if not nums:
        #     return 0
            
        # write = 1
        # prev = nums[0]  # Local variable cache: avoids dict/attribute lookups
        
        # for x in nums[1:]:
        #     if x != prev:
        #         nums[write] = x
        #         prev = x
        #         write += 1
                
        # return write
        
        
        
        # nums[:] = sorted(set(nums))
        # return len(nums)




        #return len(list(set(nums))) #it won't work because of it doesn't modify the nums in-place and it voilates O(1) 