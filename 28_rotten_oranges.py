from collections import deque 
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        fresh = 0 
        dq = deque()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 2:
                    dq.append((i, j, 0))
                elif A[i][j] == 1:
                    fresh += 1 
        time = 0 
        while dq:
            i, j, t = dq.popleft()
            time = t 
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in dirs:
                ni = i + dx
                nj = j + dy 
                if 0<=ni<n and 0<=nj<m and A[ni][nj] == 1:
                    A[ni][nj] = 2 
                    dq.append((ni, nj, t+1))
                    fresh -=1 
        if fresh == 0:
            return time 
        return -1 




        