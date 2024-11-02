class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    q = deque([(i, j)])
                    area = 0
                    while q:
                        x, y = q.pop()
                        area += 1
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                continue
                            if visited[nx][ny]:
                                continue
                            if grid[nx][ny] != 1:
                                continue
                            visited[nx][ny] = True
                            q.append((nx, ny))
                    max_area = max(max_area, area)
        return max_area
