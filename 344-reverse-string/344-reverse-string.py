class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # swapping letters
        for i in range(len(s)//2):
            print (i)
            temp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = temp
        