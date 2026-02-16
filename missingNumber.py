class Solution(object):
    def missingNumber(self,nums):
        n=len(nums)
        result=n*(n+1)//2
        return result-sum(nums)

