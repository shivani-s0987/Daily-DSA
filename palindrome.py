class Solution(object):
    def palindrome(self,x):
        num=x
        result=0
        while num>0:
            ld=num%10
            result=result*10+id
            num=num//10
        return num==result