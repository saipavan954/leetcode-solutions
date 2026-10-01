class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        is_prime = [True]*( right + 1 )
        is_prime[0] = is_prime[1] = False       
        for i in range( 2 , int(right**0.5)+1 ) :
            if is_prime[i]:
                for j in range( i*i , right + 1 , i ):
                    is_prime[j] = False
        ans = [-1 , -1]
        best = float('inf')
        prev = -1
        for p in range ( max ( left , 2 ) , right + 1 ):
            if is_prime[p] :
                if prev != -1 and p - prev < best:
                    best = p - prev 
                    ans = [prev , p ] 
                prev = p
        return ans 


        