class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                else:
                    num = board[i][j]
                    row_str = f"{num}@row{i}"
                    col_str = f"{num}@col{j}"
                    cont_str = f"{num}@cont{i//3}{j//3}"
                    if row_str in seen or col_str in seen or cont_str in seen:
                        return False
                    else:
                        seen[row_str] = 1
                        seen[col_str] = 1
                        seen[cont_str] = 1
        return True
                    
