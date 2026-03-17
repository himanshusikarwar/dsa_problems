class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        sqrt_n = int(n**0.5)
        cnt = 0 
        for i in range(1, sqrt_n+1):
            if n%i == 0:
                if i != n//i:
                    cnt += 2
                    if cnt > 2 :
                        return 0 
                else:
                    cnt += 1
        if cnt == 2:
            return 1 
        else:
            return 0 

        