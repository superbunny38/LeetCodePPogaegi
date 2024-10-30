from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(cur_idx,swap_idx):
            tmp = nums[cur_idx]
            nums[cur_idx] = nums[swap_idx]
            nums[swap_idx] = tmp
        k = 0
        count_dict = defaultdict(int)
        cur_idx, swap_idx = 0,0
        while swap_idx < len(nums):
            
            if count_dict[nums[cur_idx]]>=2:
                while count_dict[nums[swap_idx]]>=2:
                    swap_idx +=1
                    if swap_idx >= len(nums):
                        return cur_idx
                swap(cur_idx,swap_idx)
                
            count_dict[nums[cur_idx]] +=1
            cur_idx +=1
            swap_idx +=1
            k +=1
            # print("nums:",nums)
            # print(f"cur_idx:{cur_idx} swap_idx:{swap_idx}")
            # print("count_dict:",count_dict)
            
        return cur_idx
