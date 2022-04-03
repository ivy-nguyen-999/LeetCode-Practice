class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find the first decreasing element from the right
        i = len(nums) - 2
        
        # stop when nums[i+1] > nums[i]
        while(i >= 0 and nums[i] >= nums[i+1]):
            i -= 1
        
        # swap nums[i] and nums[i+1] if i >= 0
        if(i >= 0):
            j = len(nums) - 1
            while (j >= 0 and nums[j] <= nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse element from i + 1
        i += 1
        j = len(nums) - 1
        while(i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1