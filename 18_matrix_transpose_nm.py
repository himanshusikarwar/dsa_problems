class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        ans = []
        for j in range(m):
            col = []
            for i in range(n):
                col.append(A[i][j])
            ans.append(col)
        return ans 