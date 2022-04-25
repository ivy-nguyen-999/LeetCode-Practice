class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from the last
        current_index = m + n - 1
           
        # looping
        while(current_index > -1):
            
            if (m-1) >= 0 and ((n-1) < 0 or nums1[m-1] > nums2[n-1]):
                nums1[current_index] = nums1[m-1]
                m -= 1
            else:
                nums1[current_index] = nums2[n-1]
                n -= 1
            
            # decrement the index
            current_index -= 1
        
        