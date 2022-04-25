class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m] # a copy of nums1
        
        currentInt = 0
        currentNums1 = 0
        currentNums2 = 0
        
        while (currentInt < len(nums1)):
            is_nums1_exhausted = currentNums1 >= m
            is_nums2_exhausted = currentNums2 >= n
            
            if(not is_nums1_exhausted) and (is_nums2_exhausted or temp[currentNums1] < nums2[currentNums2]):
                nums1[currentInt] = temp[currentNums1]
                currentNums1 += 1
            else:
                nums1[currentInt] = nums2[currentNums2]
                currentNums2 += 1
            
            currentInt += 1
        
        