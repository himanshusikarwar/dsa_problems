class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, n, B, A):
        pf = [0] * n 
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if i == 0:
                    cur_sum = pf[j]
                else:
                    cur_sum = pf[j] - pf[i-1]
                if cur_sum <=B:
                    ans = max(ans, cur_sum)
        return ans 
        
        