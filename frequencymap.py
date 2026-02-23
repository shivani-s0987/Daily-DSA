class Solution(onject):
    def frequencyMap(self,nums):
        frequence={} or dict()
        for i in range(0,len(nums)):
            if nums[i] in frequence:
                frequence[nums[i]]+=1
            else:
                frequence[nums[i]]=1
        return frequence