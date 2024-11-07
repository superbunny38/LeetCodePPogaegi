class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums = [0]+nums+[0]
        # print("nums: ", nums)
        left_idx, right_idx = 0,0
        cur_sum = 0
        min_length = float('inf')
        while right_idx < len(nums)-1:
            # print("min length:",min_length,"left_idx:",left_idx,"right_idx:",right_idx)
            if cur_sum < target:
                right_idx += 1
                cur_sum += nums[right_idx]
            else:
                while cur_sum >= target:
                    cur_length = right_idx - left_idx + 1
                    min_length = min(min_length, cur_length)
                    cur_sum -= nums[left_idx]
                    left_idx += 1
            
            # if left_idx == right_idx == len(nums)-1:
            #     if cur_sum>=target:
            #         cur_length = right_idx - left_idx + 1
            #         min_length = min(min_length, cur_length)
            #     break
                    
        return min_length if min_length!=float('inf') else 0
