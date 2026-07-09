class Solution:
    # @param A : integer
    def solve(self, A):
        def prt(A):
            if A==0:
                return 
            prt(A-1)
            print(A, end= ' ')
        prt(A)
        print()
        return 
