class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        cnt = 0 
        def form_island(i, j):
            A[i][j] = -1 
            dirs = [(1,0), (1,1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
            for dx, dy in dirs:
                ni = i + dx
                nj = j + dy 
                if 0<=ni<n and 0<=nj<m and A[ni][nj] == 1:
                    form_island(ni, nj)
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    cnt += 1
                    form_island(i,j)
        return cnt 

        