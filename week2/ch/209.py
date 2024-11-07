class Solution:
    def minSubArrayLen(self, target, nums):
        
        left_idx = 0
        cur_sum = 0
        min_length = float('inf')
        
        for right_idx in range(len(nums)):
            cur_sum += nums[right_idx]
            while cur_sum >= target:
                cur_length = right_idx - left_idx + 1
                min_length = min(min_length, cur_length)
                cur_sum -= nums[left_idx]
                left_idx += 1
                    
        return min_length if min_length!=float('inf') else 0
