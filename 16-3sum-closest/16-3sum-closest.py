class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # for small case
        if len(nums) == 3:
            return sum(nums)
        
        #for larger cases
        nums = sorted(nums)
        
        # for target is too small
        threeSum = sum(nums[:3])
        if threeSum >= target:
            return threeSum
        
        #for target is too large
        threeSum = sum(nums[-3:])
        if threeSum <= target:
            return threeSum
        
        minDiff = 10**4 + 1
        result = 0
        
        for i in range(len(nums) - 2):
            
            #skip duplicated values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while(j < k):
                threeSum = nums[i] + nums[j] + nums[k]
                diff = abs(threeSum - target)
                
                # record the min difference
                if diff < minDiff:
                    minDiff = diff
                    result = threeSum
                
                if threeSum == target:
                    return target
                elif threeSum > target:
                    # decrement k
                    k -= 1
                    # skip duplicated values
                    while(j < k and nums[k] == nums[k + 1]):
                        k -= 1
                else:
                    # increment j
                    j += 1
                    # skip duplicated values
                    while(j < k and nums[j] == nums[j - 1]):
                        j += 1
        
        return result