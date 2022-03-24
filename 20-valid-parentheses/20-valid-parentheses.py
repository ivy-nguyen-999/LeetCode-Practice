class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        
        for new in s:
            if new == '(' or new == '[' or new == '{':
                parentheses.append(new)
            
            else:
                if (len(parentheses) == 0):
                    return False
                    
                if (ord(parentheses[-1]) == ord(new) - 2) or (ord(parentheses[-1]) == ord(new) - 1):
                    parentheses.pop()
                
                else:
                    return False
        
        if(len(parentheses) > 0):
            return False
        
        return True
        