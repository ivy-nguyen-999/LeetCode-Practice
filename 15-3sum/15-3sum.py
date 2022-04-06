class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return []
        
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            # need negative numbers to cancel out positive numbers
            if(nums[i] > 0):
                break
                
            # skip duplicated values
            if(i > 0 and nums[i] == nums[i-1]):
                continue
                
            j = i + 1 # next number to i
            k = len(nums) - 1 # last number in the list
            
            while(j < k):
                #calculate the sum
                threeSum = nums[j] + nums[k] + nums[i]
                
                # increment j if the 3sum less than 0
                if(threeSum < 0):
                    j += 1
                    
                # decrement k if the 3sum greater than 0
                elif(threeSum > 0):
                    k -= 1
                
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    # increment j value
                    j += 1
                    # decrement k value
                    k -= 1
                    # skip all duplicated values
                    while(j < k and nums[j] == nums[j - 1]):
                        j += 1
                    while(j < k and nums[k] == nums[k + 1]):
                        k -= 1

        return result