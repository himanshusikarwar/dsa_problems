class Solution:
    # @param A : list of integers
    # @return an integer
    def maxProfit(self, A):
        ans = 0 
        n = len(A)
        for i in range(1, n):
            cnt = A[i] - A[i-1]
            if cnt > 0:
                ans += cnt 
        return ans         
        