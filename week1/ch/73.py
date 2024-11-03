class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix),len(matrix[0])
        save_rows = [False]*n
        save_cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    save_rows[i] = True
                    save_cols.add(j)
        
        for idx,val in enumerate(save_rows):
            if val == True:
                matrix[idx] = [0]*m
            else:
                for col in save_cols:
                    matrix[idx][col] = 0
