class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        if len(nums) == 1:
            return True
        
        if len(nums) == 2:
            if nums[0]>0:
                return True
            else:
                return False
        
        if nums[0] == 0:
            return False
        else:
            dp[0] = True

        for idx, avail_step in enumerate(nums):
            if dp[idx]:
                if avail_step == 0:
                    continue
                else:
                    for take_step in range(1,avail_step+1):
                        if take_step+idx<len(dp):
                            dp[take_step+idx]=True
                            if take_step+idx == len(dp)-1:
                                return True
                        else:
                            break
            else:
                return False

        return dp[-1]
