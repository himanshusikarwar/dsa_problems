class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0 
        for i in range(n):
            ans += A[i][i]
        return ans 
            
        