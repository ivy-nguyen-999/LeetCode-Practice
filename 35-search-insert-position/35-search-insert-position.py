class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return index if the target in the list
        if target in nums:
            return nums.index(target)
        # append the target to the list
        # sort the list
        # return index of the target
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)