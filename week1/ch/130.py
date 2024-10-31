class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board),len(board[0])
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        

        def dfs(start_x,start_y):
            visited = [[False]*m for _ in range(n)]
            paths = [(start_x,start_y)]
            to_color = [(start_x,start_y)]
            if start_x == 0 or start_x == n-1 or start_y == 0 or start_y == m-1:
                visited[start_x][start_y] = True
                return
            while paths:
                path = paths.pop(0)
                cur_x,cur_y = path[0],path[1]
                
                for move_x,move_y in dirs:
                    new_x,new_y = cur_x+move_x,cur_y+move_y
                    if 0<=new_x<n and 0<=new_y<m:
                        if board[new_x][new_y] == 'O' and visited[new_x][new_y] == False:
                            if new_x == 0 or new_x == n-1 or new_y == 0 or new_y == m-1:
                                print("not surrounded!")
                                visited[new_x][new_y] = True
                                return
                            else:
                                visited[new_x][new_y] = True
                                print(f"marking visited true: ({new_x},{new_y})")
                                to_color.append((new_x,new_y))
                                #print("to_color:",to_color)
                                paths.append((new_x,new_y))
                        
            for color_x,color_y in to_color:
                board[color_x][color_y] = 'X'
            print("to_color:",to_color)
            return

        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j] == 'O':
                    print("\nvisiting:",i,",",j)
                    dfs(i,j)
