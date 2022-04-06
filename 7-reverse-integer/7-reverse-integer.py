class Solution:
    def reverse(self, x: int) -> int:
        # one number
        if x > -10 and x < 10:
            return x
        
        result = 0
        # negative number
        if x < 0:
            result = -int((str(x)[1:])[::-1])
        # positive number
        else:
            result = int(str(x)[::-1])
        # out of range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result