class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        #creating a graph 
        graph = [[] for _ in range(A+1)]
        for u, v in B:
            graph[u].append(v)
        #visited -- dfs so we do not get caught in infinite loop 
        #ispath -- to detect the cycle 
        visited = [0] * (A+1)
        is_path = [0] * (A+1) 
        def is_cycle(u): 
            visited[u] = 1
            is_path[u] = 1 
            for v in graph[u]:
                if is_path[v]:
                    return 1 
                if visited[v] == 0:
                    if is_cycle(v):
                        return 1
            is_path[u] = 0 
            return 0 
        for u in range(1, A+1):
            if visited[u] == 0:
                if is_cycle(u):
                    return 1            
        return 0        