class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            # skip if the current number equal the previous one
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1 # next number to i
            k = len(nums) - 1 # last number in the list
            while(j < k):
                twoSum = nums[j] + nums[k]
                if(twoSum + nums[i] == 0):
                    result.append([nums[i], nums[j], nums[k]])
                    # increment j value
                    j += 1
                    # skip all duplicated value
                    while(j < k and nums[j] == nums[j-1]):
                        j += 1
                # increment j if the 3sum less than 0
                elif(twoSum + nums[i] < 0):
                    j += 1
                # decrement k if the 3sum greater than 0
                else:
                    k -= 1
        return result