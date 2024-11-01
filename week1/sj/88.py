class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        ptr, ptr1, ptr2 = 0, 0, 0
        while ptr1 < m and ptr2 < n:
            if nums1_copy[ptr1] < nums2[ptr2]:
                nums1[ptr] = nums1_copy[ptr1]
                ptr1 += 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 += 1
            ptr += 1
        while ptr1 < m:
            nums1[ptr] = nums1_copy[ptr1]
            ptr1 += 1
            ptr += 1
        while ptr2 < n:
            nums1[ptr] = nums2[ptr2]
            ptr2 += 1
            ptr += 1
        
