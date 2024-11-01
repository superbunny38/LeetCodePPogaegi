class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                continue
                            if grid[nx][ny] == "0":
                                continue
                            if visited[nx][ny]:
                                continue
                            q.append((nx, ny))
                            visited[nx][ny] = True
                    islands += 1
        return islands
                    
