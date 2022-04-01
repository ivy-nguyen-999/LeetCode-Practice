class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # sort the combined list
        nums = sorted(nums1 + nums2)
        # simple case (no element)
        if(len(nums) == 0):
            return 0
        # if len > 0
        median = len(nums)//2
        if(len(nums) % 2 == 0):
            return(nums[median-1] + nums[median])/2
        else:
            return nums[median]