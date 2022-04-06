class Solution:
    def maxArea(self, height: List[int]) -> int:
        # handle small case:
        if(len(height) == 2):
            return min(height[0], height[1])
        
        # if len(height) > 2:
        maxWater = 0
        # left and right pointers
        left = 0
        right = len(height) - 1
        
        while(left < right):
            
            minHeight = min(height[left], height[right])
            maxWater = max(maxWater, minHeight * (right - left))
            
            # increment left or right
            # skip all line that is less than the current line
            while(minHeight >= height[left] and left < right):
                left += 1
            while(minHeight >= height[right] and left < right):
                right -= 1
                
        return maxWater
        
        
        
        
        