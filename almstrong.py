class Solution(object):
    def almstrong(self,n):
        x=n
        total=0
        nod=len(str(n))
        while x>0:
            ld=x%10
            total=total+(ld**nod)
            x=x//10
        return total==n