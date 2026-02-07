class Solution(object):
    def mergesort(self,nums1,m,nums2,n):
        a=m-1
        b=n-1
        k=m+n-1
        while b>=0:
            if a>=0 and nums1[a]>=nums2[b]:
                nums1[k]=nums1[a]
                a-=1
            else:
                nums1[k]=nums2[b]
                b-=1
            k-=1
