class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        merged=sorted(nums1+nums2)
        m=len(merged)
        mid=m//2
        if m%2==1:
            return merged[mid]
        else:
            return(merged[mid-1]+merged[mid])/2.0
