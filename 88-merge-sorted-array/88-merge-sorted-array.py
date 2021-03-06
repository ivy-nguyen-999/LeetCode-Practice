class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from the last
        current_index = m + n - 1
        # looping
        while(current_index >= 0):
            # if nums1 is not exhausted and
            # nums2 is exhausted or current nums1 > current nums2
            if m > 0 and (n < 1 or nums1[m-1] > nums2[n-1]):
                # add current nums1 to the list
                nums1[current_index] = nums1[m-1]
                m -= 1
            else:
                # add current nums2 to the list
                nums1[current_index] = nums2[n-1]
                n -= 1
            # decrement the index
            current_index -= 1
        
        