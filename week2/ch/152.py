class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = []
        min_dp = []
        for num in nums:
            if len(max_dp)==0 and len(min_dp) == 0:
                max_dp.append(num)
                min_dp.append(num)
            else:
                max_dp_item = max(max_dp[-1]*num,num,min_dp[-1]*num)
                min_dp_item = min(max_dp[-1]*num,num,min_dp[-1]*num)
                max_dp.append(max_dp_item)
                min_dp.append(min_dp_item)

        return max(max_dp)
