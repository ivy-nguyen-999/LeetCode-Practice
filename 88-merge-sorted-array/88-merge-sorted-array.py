class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        current_index = m + n - 1
        current_nums1_index = m - 1
        current_nums2_index = n - 1
        
        while(current_index >= 0):
            is_nums1_exhausted = current_nums1_index < 0
            is_nums2_exhausted = current_nums2_index < 0
            
            if(not is_nums1_exhausted) and (is_nums2_exhausted or nums1[current_nums1_index] > nums2[current_nums2_index]):
                nums1[current_index] = nums1[current_nums1_index]
                current_nums1_index -= 1
            else:
                nums1[current_index] = nums2[current_nums2_index]
                current_nums2_index -= 1
            
            current_index -= 1
        
        