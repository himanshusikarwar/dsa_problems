class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        ans = []
        for i in range(n):
            for j in range(i,n):
                cur = []
                for k in range(i, j+1):
                    cur.append(A[k])
                ans.append(cur)
        return ans 

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        ans = []
        for i in range(n):
            for j in range(i,n):
                ans.append(A[i:j+1])
        return ans 
        

        
        