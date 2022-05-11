class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) < 2):
            return len(nums)
        
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                if length > longest:
                    longest = length
        
        return longest
        