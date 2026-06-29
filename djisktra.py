import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        graph = [[] for _ in range(A)]
        for u, v, w in B:
            graph[u].append((w, v))
            graph[v].append((w, u))
        dist = [(float('inf'))]*A
        pq = []
        heapq.heappush(pq, (0, C))
        while pq:
            d_u_c,u=heapq.heappop(pq)
            if d_u_c <= dist[u]:
                dist[u] = d_u_c
                for d_v_u, v in graph[u]:
                    if d_u_c + d_v_u < dist[v]:
                        heapq.heappush(pq, (d_u_c + d_v_u, v))
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist 





        
        