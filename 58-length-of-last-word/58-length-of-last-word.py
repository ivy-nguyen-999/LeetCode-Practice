class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listStr = s.split()
        return len(listStr[-1])