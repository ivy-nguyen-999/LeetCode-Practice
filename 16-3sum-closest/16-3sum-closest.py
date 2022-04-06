class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # for small case
        if len(nums) == 3:
            return sum(nums)
        
        #for larger cases
        nums = sorted(nums)
        greater = 3001
        less = -3001
        
        for i in range(len(nums) - 2):
            
            #skip duplicated values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while(j < k):
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == target:
                    return target
                elif threeSum > target:
                    greater = min(threeSum, greater)
                    # decrement k
                    k -= 1
                    # skip duplicated values
                    while(j < k and nums[k] == nums[k + 1]):
                        k -= 1
                else:
                    less = max(threeSum, less)
                    # increment j
                    j += 1
                    # skip duplicated values
                    while(j < k and nums[j] == nums[j - 1]):
                        j += 1
        
        if abs(greater - target) < abs(less - target):
            return greater
        
        return less