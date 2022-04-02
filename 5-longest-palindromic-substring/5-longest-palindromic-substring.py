class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start = 0
        length = 1
        for current in range(1, len(s)):
            left = current - length
            right = current + 1
            
            s1 = s[left-1 : right]
            s2 = s[left : right]
            if s1 == s1[::-1] and left - 1 >= 0:
                start = left - 1
                length += 2
            elif s2 == s2[::-1]:
                start = left
                length += 1
            
        return s[start : start+length]
    
    """
    # palindrome can be even or odd. Adding # in between letters
    # in the string make all palindrome become odd palindrome
    def oddPalindrome(self, s):
        new = "#"
        for letter in s:
            new += letter + "#"
        return new
    
    # remove all # before return the palindrome
    def palindrome(self, substr):
        return substr[1::2]
    
    # manacher's algorithm
    def longestPalindrome(self, s: str) -> str:
        
        if(len(s) == 1 or s == s[::-1]):
            return s
        
        s = self.oddPalindrome(s) # len becomes 2n + 1
        
        # initialize an array to contain the length of all palindromes
        P = [0] * (len(s))
        
        # variable to store index of the final center
        finalCenter = 0
        maxLen = 0
        
        # variables to contain the current center and its right boundary
        center = 0
        right = 0
        
        # loop while the current center is valid
        for index in range(len(s)):
            # find mirror of index 
            mirror = 2 * center - index
            
            # if the index is less than the right boundary
            if (index < right):
                P[index] = min(right - index, P[mirror])
            
            # find the largest palindrome around this center
            iRight = index + P[index] + 1
            iLeft = index - P[index] - 1
            while(iRight < len(s) and iLeft >= 0 and s[iRight] == s[iLeft]):
                P[index] += 1
                iRight += 1
                iLeft -= 1
            
            # if the palindome expands beyond the right boundary of the current
            # palindrome at the center
            if(index + P[index] > right):
                # update new center
                center = index
                right = index + P[index]
                # update the final substring if needed
                if (P[index] > maxLen):
                    finalCenter = index
                    maxLen = P[index]
        
        result = s[finalCenter - maxLen: finalCenter + maxLen + 1]
        return self.palindrome(result)
    """
    

            