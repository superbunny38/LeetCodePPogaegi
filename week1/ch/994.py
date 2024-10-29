class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        
        def dfs():
            visited = [[False]*m for _ in range(n)]
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            is_change = False
            is_fresh = False
            for i in range(n):
                for j in range(m):
                    if visited[i][j] == False and grid[i][j] == 2:
                        for move_x,move_y in dirs:
                            new_x,new_y = i+move_x,j+move_y
                            if 0<=new_x<n and 0<=new_y<m:
                                if grid[new_x][new_y] == 1:
                                    grid[new_x][new_y] = 2
                                    visited[new_x][new_y] = True
                                    is_change = True
                    if grid[i][j] == 1:
                        is_fresh = True
                                    
            return is_change, is_fresh
        
        n_time = 0
        while True:
            ch, fr = dfs()
            if ch == False:
                break
            else:
                n_time +=1
        if fr:
            return -1
        else:
            return n_time
