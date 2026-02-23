class Solution(object):
    #n={5,6,4,3,5,2,6,8,9,7,9}
    #m={10,33,5,6,4,2,6,8,9,5} chejing the m vales in n and retuen how many time the m values in n
    def countMatches(self,n,m):
        for i in m:
            count=0
            for j in n:
                if i==j:
                    count+=1
        return count
             

