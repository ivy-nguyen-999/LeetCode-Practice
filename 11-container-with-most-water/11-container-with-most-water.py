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
            maxWater = max(maxWater, min(height[left], height[right]) * (right - left))
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return maxWater
        
        
        
        
        