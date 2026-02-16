class Solution(object):
    def missingNumber(self,nums):
        l=len(nums)
        result=l*(l+1)//2
        return result-sum(nums)

