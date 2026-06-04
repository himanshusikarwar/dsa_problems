class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # creating a directed graph
        graph = [[] for _ in range(A+1)]
        for u, v in B:
            graph[u].append(v)
        visited = [0] * (A+1)
        def is_path(u, A):
            if u == A:
                return 1 
            visited[u] = 1
            for v in graph[u]:
                if visited[v] == 0:
                    if is_path(v, A):
                        return 1 
            return 0 
        return is_path(1, A)


        