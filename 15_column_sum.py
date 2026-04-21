class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        ans = []
        for j in range(m):
            col_sum=0
            for i in range(n):
                col_sum += A[i][j]
            ans.append(col_sum)
        return ans
            


        
        