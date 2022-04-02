class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to string
        string = str(x)
        return string == string[::-1]