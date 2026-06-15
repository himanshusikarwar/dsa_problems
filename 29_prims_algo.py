import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = [[] for _ in range(A+1)]
        for u, v, w in B:
            graph[u].append((w, v))
            graph[v].append((w, u))
        pq = []
        ans = 0 
        heapq.heappush(pq, (0, 1))
        visited = [0]*(A+1)
        while pq:
            wt, u = heapq.heappop(pq)
            if visited[u] == 0:
                ans += wt 
                visited[u] = 1 
                for w_v, v in graph[u]:
                    if visited[v] == 0:
                        heapq.heappush(pq, (w_v, v))
        return ans 
