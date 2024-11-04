class Vertex:
    def __init__(self, v = None, dist = 0):
        self.v = v
        self.dist = dist

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def find_coord(number):
        
            row_idx = n-(number-1)//(n)-1#5 = 6-(2-1)//6-1 = 6-3-1
            max_num_in_row = (n-row_idx)*n#(6-5)*6=6
            min_num_in_row = max_num_in_row-(n-1)
            if n%2 == 0:
                if row_idx%2 == 1:#[5][1] = 2, [1][0]=25 
                    col_idx = number-min_num_in_row
                else:#[4][1] = 11, #[2][0] = 24
                    col_idx = max_num_in_row-number
            else:
                if row_idx%2 == 1:
                    col_idx = max_num_in_row-number
                else:
                    col_idx = number-min_num_in_row
            return row_idx,(col_idx)%n
            
            
        starting_point = Vertex(1,0)
        queue = [starting_point]
        visited = [False]*(n**2+1)
        
        while queue:
            point = queue.pop(0)
            if point.v == n*n:
                return point.dist
            
            for dice_roll in range(1,6+1):
                try_v = dice_roll + point.v
                if try_v <= n*n and visited[try_v] == False:
                    visited[try_v] = True
                    try_x,try_y = find_coord(try_v)
                    # print(f"found:{try_v} at {try_x},{try_y}")
                    new_dist = point.dist+1
                    new_point = Vertex(try_v,new_dist)
                    
                    if board[try_x][try_y] != -1:
                        new_v = board[try_x][try_y]
                        new_point.v = new_v
                    queue.append(new_point)    
        return -1
            
