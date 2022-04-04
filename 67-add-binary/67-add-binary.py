class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # reverse strings
        a, b = a[::-1], b[::-1]
        
        # let b be the shorter string
        if len(b) > len(a):
            a, b = b, a
        
        # make all string equal
        a = a + "0"
        b = b + "0" * (len(a) - len(b))
        
        # start adding
        result = ""
        remainder = "0"
        
        for index in range(len(b)):
            if a[index] == "0":
                if b[index] == "0":
                    # 0 0 0 and 0 0 1
                    result = remainder + result
                    # reset remainder
                    remainder = "0"
                else: # b[index] == "1"
                    # 0 1 0
                    if remainder == "0":
                        result = "1" + result
                    else: # 0 1 1
                        result = "0" + result
                        remainder = "1"
            else: # a[index] == "1"
                if b[index] == "0":
                    # 1 0 0
                    if remainder == "0":
                        result = "1" + result
                    else: # 1 0 1
                        result = "0" + result
                        remainder = "1"
                else: # b[index] == "1"
                    # 1 1 0
                    if remainder == "0":
                        result = "0" + result
                    else: # 1 1 1
                        result = "1" + result
                    remainder = "1"
        
        if(result[0] == "0"):
            return result[1:]
        
        return result
                