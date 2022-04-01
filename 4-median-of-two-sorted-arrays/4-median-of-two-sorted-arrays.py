class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combine 2 lists
        for element in nums2:
            nums1.append(element)
        # sort the combined list
        nums1 = sorted(nums1)
        # simple case (no element)
        if(len(nums1) == 0):
            return 0
        # if len > 0
        median = len(nums1)//2
        if(len(nums1) % 2 == 0):
            return(nums1[median-1] + nums1[median])/2
        else:
            return nums1[median]