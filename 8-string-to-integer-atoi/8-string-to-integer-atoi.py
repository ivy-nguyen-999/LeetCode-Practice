class Solution:
    def myAtoi(self, s: str) -> int:
        # ignore any leading whitespace
        s = s.strip()
        
        num = ""
        for char in s:
        # get the sign and numbers
            if (ord(char) > 47 and ord(char) < 58):
                num += char
            else:
                if (char == "-" or char == "+") and num == "":
                    num += char
                else:
                    break
        
        # if the string is empty
        if num == "" or num == "-" or num == "+":
            return 0
        else:
            result = int(num)
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            else:
                return result