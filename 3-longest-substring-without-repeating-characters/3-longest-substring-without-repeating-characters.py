class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # simple cases len(s) = 1 or 0
        if(len(s) < 2):
            return len(s)
        # sliding windows
        result = 0
        i = 0
        for j in range(len(s)):
            substr = s[i:j]
            # if this letter is in the current word
            # slide the window if there is a duplicate
            if s[j] in substr:
                #string.find("substring", start, end)
                i = s.find(s[j],i,j) + 1
            #calculate len of the substring
            tempLen = j - i + 1
            if(tempLen > result):
                result = tempLen
        return result