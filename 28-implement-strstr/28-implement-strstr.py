class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #The find() method returns the index of first occurrence 
        # of the substring (if found). If not found, it returns -1.
        return haystack.find(needle)