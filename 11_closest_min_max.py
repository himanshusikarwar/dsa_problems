class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_A = max(A)
        min_A = min(A) 
        max_idx = -1 
        min_idx = -1 
        n = len(A)
        ans = float('inf')
        for i in range(n):
            if A[i] == min_A:
                min_idx = i 
            if A[i] == max_A:
                max_idx = i 
            if max_idx != -1 and min_idx != -1:
                ans = min(ans, abs(max_idx-min_idx) + 1)
        return ans if ans != float('inf') else 0 
        # if ans == float('inf'):
        #     return 0 
        # else:
        #     return ans


