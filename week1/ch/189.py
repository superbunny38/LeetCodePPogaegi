class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse(start_idx,end_idx):
            left,right = start_idx, end_idx
            while left < right:
                #print(f"left:{left} right:{right}")
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1

        reverse(0,len(nums)-k-1)#reverse first half
        print()
        reverse(len(nums)-k,len(nums)-1)#reverse last half
        print()
        reverse(0,len(nums)-1)#reverse all
