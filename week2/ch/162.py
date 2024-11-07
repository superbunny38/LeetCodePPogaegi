import sys
sys.setrecursionlimit(10**6)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float('inf')]+nums+[-float('inf')]
        peak_idx = int(len(nums)//2)

        def find_peak(peak_idx):
            # print("currently on:",peak_idx-1)
            if nums[peak_idx-1]<nums[peak_idx] and nums[peak_idx]>nums[peak_idx+1]:
                return peak_idx-1
            else:
                if nums[peak_idx-1]<nums[peak_idx+1]:
                    return find_peak(peak_idx+1)
                else:#nums[peak_idx-1]>nums[peak_idx+1]
                    return find_peak(peak_idx-1)
        
        return find_peak(peak_idx)
