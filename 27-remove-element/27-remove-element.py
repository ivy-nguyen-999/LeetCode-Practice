class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pointer to keep track of number of accepted values
        length = 0
        
        # loop thru each element of the list
        for index in range(len(nums)):
            # remove all occurrences of val in the list
            if(nums[index] != val):
                nums[length] = nums[index]
                # move pointer to the right
                length += 1
        
        return length