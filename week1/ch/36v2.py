class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_rows = [[False] * 9 for _ in range(9)]
        check_cols = [[False] * 9 for _ in range(9)]
        check_boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    num = int(board[i][j])
                    if check_rows[i][num-1]:
                        return False
                    check_rows[i][num-1] = True
                    if check_cols[j][num-1]:
                        return False
                    check_cols[j][num-1] = True
                    idx = (i // 3) * 3 + j // 3
                    if check_boxes[idx][num-1]:
                        return False
                    check_boxes[idx][num-1] = True
        return True
