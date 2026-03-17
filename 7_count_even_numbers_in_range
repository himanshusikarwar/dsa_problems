class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        pf = [0] * n 
        if A[0] % 2 == 0:
            pf[0] = 1
        for i in range(1, n):
            if A[i] % 2 == 0:
                pf[i] = pf[i-1] + 1
            else:
                pf[i] = pf[i-1]
        ans = []
        for l, r in B:
            if l == 0:
                ans.append(pf[r])
            else:
                ans.append(pf[r] - pf[l-1])
        return ans 


        
        