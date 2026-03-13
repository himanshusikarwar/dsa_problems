class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, k):
        A.sort()
        n = len(A)
        i = 0 
        j = n-1
        while i<j:
            cur_sum = A[i] + A[j]
            if cur_sum == k:
                return 1 
            elif cur_sum < k:
                i += 1
            else:
                j-=1 
        return 0 

        