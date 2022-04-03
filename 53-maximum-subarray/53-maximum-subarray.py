class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if there is only one element in the array
        if(len(nums) == 1):
            return nums[0]
        
        maxSum = -10**4
        currSum = 0
        
        for num in nums:
            # compare previous sum with 0
            # if it is less than 0, reset the sum to 0
            currSum = max(currSum, 0)
            # add the current number to the sum
            currSum += num
            # compare the current number with the max sum
            maxSum = max(currSum, maxSum)        
        return maxSum