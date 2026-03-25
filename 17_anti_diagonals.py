class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        ans = []
        n = len(A)
        for j in range(n):
            i = 0 
            cur = [0]*n
            k = 0
            while i < n and j >= 0:
                cur[k] = A[i][j]
                i += 1 
                j -= 1 
                k+=1
            ans.append(cur)
        for i in range(1, n):
            j = n-1 
            cur = [0]*n
            k = 0
            while i < n and j >= 0:
                cur[k] = A[i][j]
                i += 1 
                j -= 1 
                k+=1
            ans.append(cur)
        return ans 


        