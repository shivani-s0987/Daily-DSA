class Solution(object):
    def twoSum(self, nums, target):
        nums_h={}
        for i in range(len(nums)):
            seen=target-nums[i]
            if seen in nums_h:
                return[nums_h[seen],i]
            nums_h[nums[i]]=i
        
      
