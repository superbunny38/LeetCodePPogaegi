class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_count, cur_num = 1, nums[0]
        for num in nums[1:]:
            if cur_count == 0:
                cur_num = num
            if num  == cur_num:
                cur_count += 1
            else:
                cur_count -= 1
        return cur_num
                
