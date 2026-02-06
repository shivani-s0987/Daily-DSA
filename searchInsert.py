class Solution(object):
    def searchInsert(self,nums,target):
        n,m=0,len(nums)-1
        while n<=m:
            mid=(n+m)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left