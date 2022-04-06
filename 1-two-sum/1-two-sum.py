class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = [0] * len(nums)
        for i, num in enumerate(nums):
            comps[i] = target - num
        
        for num in comps:
            if num in nums:
                index = nums.index(num)
                if index != nums.index(target - num):
                    return [index, nums.index(target - num)]
                elif num in nums[index + 1:]:
                    return [index, nums.index(target - num, index + 1)]