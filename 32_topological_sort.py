import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        graph = [[] for _ in range(A+1)]
        indegree = [0] * (A+1)
        cnt = 0 
        for u, v in B:
            graph[u].append(v)
            indegree[v] += 1 
        pq = []
        for u in range(1, A+1):
            if indegree[u] == 0:
                heapq.heappush(pq, u)
        ans = []
        while pq:
            u = heapq.heappop(pq)
            ans.append(u)
            cnt += 1 
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    heapq.heappush(pq, v)
        
        if cnt != A:
            return []
        else:
            return ans 

                
            

        
        