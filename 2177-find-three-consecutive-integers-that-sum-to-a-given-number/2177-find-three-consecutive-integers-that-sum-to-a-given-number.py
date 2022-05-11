class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num % 3):
            return []
        third = num//3
        return [third - 1, third, third + 1]
        