class Solution(object):
    def palindrome(self,x):
        num=x
        result=0
        while num>0:
            ld=num%10
            result=result*10+ld
            num=num//10
        return x==result
    
#if the given number is palindrome return true else return false
n=123
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
return n==result