class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(to_explore):
            candidates = [to_explore]
            while candidates:
                candi = candidates.pop(-1)
                visited[candi] = True
                for idx, adj in enumerate(isConnected[candi]):
                    if visited[idx] == False and adj == 1:
                        candidates.append(idx)
                    
        ret = 0
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                ret += 1
        return ret
