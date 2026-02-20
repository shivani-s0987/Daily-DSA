#20
from cmath import sqrt


class Solution(object):
    def divisors(self,n):
        result=[]
        for i in range(1,n+1):
            if n%i==0:
                result.append(i)
        return result

#36/6  #25 root of number 
class Solution(object):
    def divisiors(self,num):
        result=[]
        for i in range(1,num//2+1):
            if num%i==0:
                result.append(i)
            result.append(num)
        return result 
# root of numbber
from math import sqrt
class Solution(object):
    def divisiors(self,n):
        result=[]
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                result.append(i)
                if i!=n//i:
                    result.append(n//i)
        result.sort()
        return result