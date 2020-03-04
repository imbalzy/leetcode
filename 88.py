class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        while i+j+1>=0:
            if i<0 or (j>=0 and nums2[j]>nums1[i]):
                nums1[i+j+1]=nums2[j]
                j-=1
            else:
                nums1[i+j+1]=nums1[i]
                i-=1
