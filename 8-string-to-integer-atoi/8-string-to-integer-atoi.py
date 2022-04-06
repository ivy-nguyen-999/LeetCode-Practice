class Solution:
    def myAtoi(self, s: str) -> int:
        # ignore any leading whitespace
        s = s.lstrip()
        
        num = ""
        for char in s:
            # get the sign and numbers using ascii
            if (ord(char) >= 48 and ord(char) <= 57):
                num += char
            else:
                if (ord(char) == 43 or ord(char) == 45) and not num:
                    num += char
                else:
                    break
        
        # if the string is empty
        if num == "" or num == "-" or num == "+":
            return 0
        else:
            result = int(num)
            if result >= -pow(2,31) and result <= pow(2,31) - 1:
                return result
            elif result < 0:
                 return -pow(2,31)
            else:
                return pow(2,31) - 1
                