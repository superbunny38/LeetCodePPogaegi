class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        n_paths = [[0]*n for _ in range(m)]
        for i in range(m):
            n_paths[i][0] = 1

        for j in range(n):
            n_paths[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                n_paths[i][j] = n_paths[i-1][j]+n_paths[i][j-1]
        return n_paths[m-1][n-1]
