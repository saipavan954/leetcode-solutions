class Solution:
    def smallestValue(self, n: int) -> int:
        while True :
            x , s , p = n , 0 , 2 
            while p * p <= x :
                while x % p == 0 :
                    s += p 
                    x //=p
                p += 1
            if x > 1:
                s += x
            if s == n:
                return n
            n = s
            


        
        