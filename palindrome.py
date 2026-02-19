class Solution(object):
    def palindrome(self,nums):
        x=nums
        result=0
        while nums>0:
            digit=nums%10
            result=result*10+digit
            nums=nums//10
        return x==result
            