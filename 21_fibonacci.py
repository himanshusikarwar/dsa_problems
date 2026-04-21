import sys 
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        def fib(n):
            # if n == 0:
            #     return 0 
            # if n == 1:
            #     return 1 
            if n == 0 or n == 1:
                return n
            ans = fib(n-1) + fib(n-2)
            return ans
        return fib(A)
        
        