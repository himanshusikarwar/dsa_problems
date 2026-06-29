from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        graph = [[] for _ in range(A+1)]
        indegree = [0] * (A+1)
        cnt = 0 
        for i in range(len(B)):
            u = B[i]
            v = C[i]
            indegree[v] +=1 
            graph[u].append(v)
        dq = deque()
        for u in range(1, A+1):
            if indegree[u] == 0:
                dq.append(u)
        
        while dq:
            u = dq.popleft()
            cnt += 1 
            for v in graph[u]:
                indegree[v] -= 1 
                if indegree[v] == 0:
                    dq.append(v)
        if cnt == A:
            return 1 
        else:
            return 0 
        


                