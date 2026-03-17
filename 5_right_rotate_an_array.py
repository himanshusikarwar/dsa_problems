class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        B = B%n
        def reverse(A, i, j):
            while i<j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        reverse(A, n-B, n-1)
        reverse(A, 0, n-B-1)        
        reverse(A, 0, n-1)
        return A