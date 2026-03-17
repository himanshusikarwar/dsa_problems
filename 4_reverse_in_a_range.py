class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, i, j):
        while i<j:
            A[i], A[j] = A[j], A[i]
            i+=1 
            j-=1
        return A        
        