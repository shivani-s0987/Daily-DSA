class Solution(object):
    def frequencyMap(self,nums):
        frequence={} # dict()
        for i in range(0,len(nums)):
            if nums[i] in frequence:
                frequence[nums[i]]+=1
            else:
                frequence[nums[i]]=1
        return frequence
    
#another method
class Solution(object):
    def frequencyMap(self,nums):
        frequence={}
        n=len(nums)
        for i in range(0,n):
            frequence[nums[i]]=frequence.get(nums[i],0)+1
        return frequence