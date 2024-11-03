class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [triangle[0][0]]
        for arr in triangle[1:]:
            new_dp = []
            print()
            for idx,num in enumerate(arr):
                if idx == 0:
                    new_dp.append(num+dp[0])
                    continue
                if idx == len(arr)-1:
                    new_dp.append(num+dp[-1])
                    continue
                new_dp.append(num+min(dp[idx],dp[idx-1]))
            dp = new_dp
        return min(dp)
