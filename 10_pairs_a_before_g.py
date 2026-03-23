class Solution:
    # @param A : string
    # @return an long
    def solve(self, A):
        n = len(A)
        cnt_a = 0
        ans = 0
        for i in range(n):
            if A[i] == 'A':
                cnt_a += 1
            elif A[i] == 'G':
                ans += cnt_a
        return ans 



class Solution:
    # @param A : string
    # @return an long
    def solve(self, A):
        n = len(A)
        ans = 0
        for i in range(n):
            if A[i] == 'G':
                j = i-1 
                cnt_a = 0 
                while j >=0:
                    if A[j] == 'A':
                        cnt_a += 1
                    j-=1
                ans += cnt_a 
        return ans 
                    



        
