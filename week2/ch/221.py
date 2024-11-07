class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])

        dp = [[0]*m for _ in range(n)]
        dp[0][0] = int(matrix[0][0])
        max_len = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                    max_len = max(max_len,dp[i][j])
                    continue
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    max_len = max(max_len,dp[i][j])
                else:
                    dp[i][j] = 0
        for d in dp:
            print(d)
        return max_len**2
