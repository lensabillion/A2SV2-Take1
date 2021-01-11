class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        repeated = {}
        """
        #O(N^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
        return  cnt
        """
        for n in nums:
           
            if n in repeated:
                cnt += repeated[n]
                repeated[n] += 1
            else:
                repeated[n] = 1
        #for i in repeated:
         #   n = repeated[i] - 1
          #  cnt += (n* (n + 1)) // 2
        return cnt
