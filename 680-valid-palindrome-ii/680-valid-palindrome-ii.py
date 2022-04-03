class Solution:
    def validPalindrome(self, s: str) -> bool:
        if(s == s[::-1]):
            return True
        # have extra letters        
        left = 0
        right = len(s) - 1
        
        while(left <= right):
            # find where it is not palindrome
            if(s[right] != s[left]):
                # remove either letter at index left or right
                s1 = s[:right] + s[right+1:]
                s2 = s[:left] + s[left+1:]
                # return true if one of them is palindrome
                if(s1 == s1[::-1] or s2 == s2[::-1]):
                    return True
                else:
                    # return False if none of them is palindrome
                    return False
            # update left and right
            left += 1
            right -= 1
            
        return True
            
        
        