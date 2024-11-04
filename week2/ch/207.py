class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            after,first = pre[0],pre[1]
            adj[first].append(after)
        
        def isCyclicrec(adj,u,visited,recStack):
            if visited[u] == False:
                visited[u] = True
                recStack[u] = True

                for x in adj[u]:
                    if visited[x] == False and isCyclicrec(adj,x,visited,recStack):
                        return True
                    elif recStack[x]:
                        return True

            recStack[u] = False
            return False

        def isCyclic(V,adj):
            visited = [False]*V
            recStack = [False]*V

            for i in range(V):
                if visited[i] == False and isCyclicrec(adj,i,visited,recStack):
                    return True
            return False

        if isCyclic(numCourses,adj)== True:
            return False
        else:
            return True
