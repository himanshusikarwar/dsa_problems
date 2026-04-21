import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def fact(n):
            if n == 0 :
                return 1 
            ans = n * fact(n-1)
            return ans 
        return fact(A)
        