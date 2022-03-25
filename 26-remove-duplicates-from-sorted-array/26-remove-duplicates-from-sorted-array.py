class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if (len(nums) == 0):
            return 0
        
        k = 0
        for index in range (1, len(nums)):
            if (nums[k] != nums[index]):
                k += 1
                nums[k] = nums[index]
        
        return k + 1
    