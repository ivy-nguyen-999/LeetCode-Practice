class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # base cases:
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            return []
        
        nums.sort()
        # for cases the target is too small or too big
        if sum(nums[:4]) > target or sum(nums[-4:]) < target:
            return []
        
        
        result = []
        
        for a in range(len(nums) - 3):
            # skip duplicated values
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # break if the sum of the next four numbers is larger than the target
            if sum(nums[a:a+4]) > target:
                break
            for b in range(a + 1, len(nums) - 2):
                # skip duplicated values
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                
                c = b + 1
                d = len(nums) - 1
                
                while(c < d):
                    fourSum = nums[a] + nums[b] + nums[c] + nums[d]
                    if fourSum == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while(c < d and nums[c] == nums[c - 1]):
                            c += 1
                        while(c < d and nums[d] == nums[d + 1]):
                            d -= 1
                    elif fourSum > target:
                        d -= 1
                        while(c < d and nums[d] == nums[d + 1]):
                            d -= 1
                    else:
                        c += 1
                        while(c < d and nums[c] == nums[c - 1]):
                            c += 1
        return result