from  math  import isqrt
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        hi = isqrt(r)
        lo = isqrt(l-1) + 1
        is_prime = [True]*(hi+1)
        is_prime[0] = is_prime[1] = False
        for i in range( 2, isqrt(hi) + 1 ):
            if is_prime[i]:
                for j in range( i * i , hi +1 , i):
                    is_prime[j] = False
        special = sum ( is_prime[p] for p in range( max(lo,2) , hi+1) ) 
        return (r+1-l) - special

        
