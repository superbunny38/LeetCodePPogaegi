class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums)-1
        min_reachable = last_idx
        for idx in range(len(nums)-2,-1,-1):
            if idx+nums[idx]>=min_reachable:
                min_reachable = idx
        return min_reachable == 0
