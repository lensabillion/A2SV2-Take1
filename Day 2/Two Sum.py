class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        for i in range(len(nums)):
            if nums[i ] not in dict:
                dict[nums[i]] = i
       
        for i in range(len(nums)):
            
            if (target - nums[i]) in dict and dict[target - nums[i]] != i:
                
                return [i,dict[target-nums[i]]]
                
