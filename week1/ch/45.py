class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        dp[0] = 0
        for idx, avail_step in enumerate(nums):
            for step in range(1,avail_step+1):
                cur_step = dp[idx]+1
                if idx+step<len(nums):
                    dp[idx+step] = min(cur_step,dp[idx+step])  
                else:
                    break
        #print(dp)
        return dp[-1]
