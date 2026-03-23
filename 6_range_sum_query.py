class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        pf = [0] * n 
        pf[0] = A[0]
        for i in range(1, n):
            pf[i] = pf[i-1] + A[i]
        ans = []
        for l, r in B:
            if l == 0:
                ans.append(pf[r])
            else:
                ans.append(pf[r]-pf[l-1])
        return ans

