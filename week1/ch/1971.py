
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = [[] for _ in range(n)]
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        s = [source]
        while s:
            popped = s.pop()
            if popped == destination:
                return True
            for adj in graph[popped]:
                if adj not in visited:
                    s.append(adj) 
                    visited.add(adj)    
        return False       
