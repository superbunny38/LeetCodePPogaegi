from collections import defaultdict
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def find_cont_id(i,j):
            if i<3:
                if j<3:
                    return 0
                elif 3<=j<6:
                    return 1
                else:
                    return 2
            elif 3<=i<6:
                if j<3:
                    return 3
                elif 3<=j<6:
                    return 4
                else:
                    return 5
            else:
                if j<3:
                    return 6
                elif 3<=j<6:
                    return 7
                else:
                    return 8

        n,m = len(board),len(board[0])

        visit_row = [False]*n
        visit_col = [False]*m
        visit_cont = [False]*9

        def check_row(row_idx):
            store = defaultdict(int)
            for num in board[row_idx]:
                if num != '.':
                    num = int(num)
                    store[num] += 1
                    if store[num]>1:
                        return False
            return True
        
        def check_col(col_idx):
            store = defaultdict(int)
            for num in np.array(board)[:,col_idx]:
                if num != '.':
                    num = int(num)
                    store[num] += 1
                    if store[num]>1:
                        return False
            return True
        
        def check_cont(cont_id):
            if cont_id == 0:
                check1d = np.array(board)[0:3,0:3].flatten()
            elif cont_id == 1:
                check1d = np.array(board)[0:3,3:6].flatten()
            elif cont_id == 2:
                check1d = np.array(board)[0:3,6:].flatten()
            elif cont_id == 3:
                check1d = np.array(board)[3:6,0:3].flatten()
            elif cont_id == 4:
                check1d = np.array(board)[3:6,3:6].flatten()
            elif cont_id == 5:
                check1d = np.array(board)[3:6,6:].flatten()
            elif cont_id == 6:
                check1d = np.array(board)[6:,:3].flatten()
            elif cont_id == 7:
                check1d = np.array(board)[6:,3:6].flatten()
            else:
                check1d = np.array(board)[6:,6:].flatten()

            store = defaultdict(int)
            for num in check1d:
                if num != '.':
                    num = int(num)
                    store[num] += 1
                    if store[num]>1:
                        return False
            return True
             

        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    if visit_row[i]:
                        pass
                    else:
                        if check_row(i):
                            visit_row[i] = True
                        else:
                            return False
                    
                    if visit_col[j]:
                        pass
                    else:
                        if check_col(j):
                            visit_col[j] = True
                        else:
                            return False
                    
                    cont_id = find_cont_id(i,j)
                    if visit_cont[cont_id]:
                        pass
                    else:
                        if check_cont(cont_id):
                            visit_cont[cont_id] = True
                        else:
                            return False
        return True    
                    
