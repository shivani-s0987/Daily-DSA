n=7437
num=n
count=0
while num>0:
    count=count+1
    num=num//10
print(count)

#another way
class Solution(object):
    def countDigits(self,n):
        count=0
        for i in str(n):
            if n%int(i)==0:
                count+=1
            return count


