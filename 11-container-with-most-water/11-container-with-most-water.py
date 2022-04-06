class Solution:
    def maxArea(self, height: List[int]) -> int:
        # handle small case:
        if(len(height) == 2):
            return min(height[0], height[1])
        
        # if len(height) > 2:
        maxWater = 0
        maxHeight = max(height)
        # left and right pointers
        left = 0
        right = len(height) - 1
        
        while(left < right):
            area = min(height[left], height[right]) * (right - left)
            maxWater = max(maxWater, area)
            # increment left or right
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
            # break if we find the maxWater
            if(maxWater>maxHeight*(right-left)):
                break
        
        return maxWater
        
        
        
        
        