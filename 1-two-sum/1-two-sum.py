class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            match = target - nums[i]
            if match in nums[i+1:]:
                return[i, nums.index(match, i + 1)]
            