class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0] * (len(digits) + 1)
        
        addOne = 1
        index = len(digits)
        
        while(addOne == 1):
            sum = addOne
            
            if((index - 1) >= 0):
                sum += digits[index - 1]
                
            if(sum < 10):
                addOne = 0
                
            result[index] = sum % 10
            index -= 1
        
        # the left over
        for i in range(1, index + 1):
            result[i] = digits[i-1]
        
        if(result[0] == 0):
            return result[1:]
        return result