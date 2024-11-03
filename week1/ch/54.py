class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        dirs = {'left':(0,-1),'right':(0,1),'down':(1,0),'up':(-1,0)}
        next_dirs = {'left':'up','right':'down','down':'left','up':'right'}
        cur_dir = ['right']
        save_togo = [(0,0)]
        visited = [[False]*m for _ in range(n)]

        def is_okay_limit(x,y):
            if 0<=x<n and 0<=y<m:
                return True
            else:
                return False

        def find_next(x,y):
            move_x,move_y = dirs[cur_dir[0]][0],dirs[cur_dir[0]][1]
            if is_okay_limit(move_x+x,move_y+y) and visited[move_x+x][move_y+y] == False:
                return (move_x+x,move_y+y)
            else:
                try_dir = next_dirs[cur_dir[0]]
                move_x,move_y = dirs[try_dir][0],dirs[try_dir][1]
                print(f"trying... {try_dir}")
                print("is_okay_limit(move_x+x,move_y+y):",is_okay_limit(move_x+x,move_y+y))
                print(f"move_x:{move_x} move_y:{move_y} x:{x} y:{y}")
                if is_okay_limit(move_x+x,move_y+y) and visited[move_x+x][move_y+y] == False:
                    cur_dir[0] = try_dir
                    return (move_x+x,move_y+y)
                else:
                    return None

        ans = []    

        while save_togo:
            cur_x,cur_y = save_togo.pop(0)
            print(f"\ncur: ({cur_x}, {cur_y}) cur_dir:{cur_dir[0]} elem: {matrix[cur_x][cur_y]}")
            ans.append(matrix[cur_x][cur_y])
            visited[cur_x][cur_y] = True
            next_move = find_next(cur_x,cur_y)
            if next_move:
                save_togo.append(next_move)
        
        return ans
