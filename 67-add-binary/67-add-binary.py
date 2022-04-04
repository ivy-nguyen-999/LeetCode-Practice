class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # reverse strings
        a, b = a[::-1], b[::-1]
        
        # let b be the shorter len string
        if len(b) > len(a):
            a, b = b, a
        
        # make all string equal
        a = a + "0"
        b = b + "0" * (len(a) - len(b))
        
        # start adding
        result = ""
        remainder = "0"
        
        for index in range(len(b)):
            if(a[index] == "0" and b[index] == "0"):
                result = remainder + result
                remainder = "0"
            elif((a[index] == "1" and b[index] == "0") or (a[index] == "0" and b[index] == "1")):
                if(remainder == "0"):
                    result = "1" + result
                else:
                    result = "0" + result
            else: # a[index] == 1 and b[index] == 1
                if(remainder == "0"):
                    result = "0" + result
                else:
                    result = "1" + result
                remainder = "1"
        
        if(result[0] == "0"):
            return result[1:]
        
        return result
                