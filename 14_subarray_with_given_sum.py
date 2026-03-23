class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        fw = 0 
        n = len(A)
        for i in range(B):
            fw += A[i]
        if fw == C:
            return 1 
        s = 1 
        e = B
        while e < n:
            fw = fw - A[s-1] + A[e]
            if fw == C:
                return 1 
            s += 1 
            e += 1 
        return 0 
        
        