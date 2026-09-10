class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        print(neg)
        print(pos)

        neg = [x*x for x in neg]
        print(neg)
        pos = [x*x for x in pos]
        print(pos)

        neg.reverse()
        print(neg)

        n = len(neg)
        m = len(pos)

        i=0
        j=0

        result = []

        while i<n and j<m:
            if neg[i] < pos[j]:
                result.append(neg[i])
                i += 1
            else:
                result.append(pos[j])
                j += 1

        print(result)

        
        while j<m:
            result.append(pos[j])
            j += 1
        
        while i<n:
            result.append(neg[i])
            i += 1

        print(result)

        return result





        # it's time complexity is n log n it is simplest solution
        # nums = [num**2 for num in nums]
        # return sorted(nums)



