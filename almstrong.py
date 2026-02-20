class Solution(object):
    def almstrong(self,num):
        x=num
        sum=0
        noi=len(str(num))
        while x>0:
            ld=x%10
            sum=sum+(ld**noi)
            x=x//10
        return sum==num
