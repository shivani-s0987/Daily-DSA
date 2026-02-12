class Solution(object):
    def mejorityElement(self,nums):
        return(max(set(nums),key=nums.count)) # set removes the duplicates