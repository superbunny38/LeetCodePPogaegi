class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        n_cycles = int(n//2)

        #upside down
        n = len(matrix)
        if n%2 == 0:
            for idx in range(int(n//2)):
                tmp = matrix[idx]
                matrix[idx] = matrix[n-1-idx]
                matrix[n-1-idx] = tmp
        else:
            for idx in range(int(n//2)):
                tmp = matrix[idx]
                matrix[idx] = matrix[n-1-idx]
                matrix[n-1-idx] = tmp
        
        #transpose
        for i in range(n-1):
            for j in range(i+1,n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
