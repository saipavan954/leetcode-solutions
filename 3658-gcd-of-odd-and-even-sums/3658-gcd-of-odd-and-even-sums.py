class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=n**2
        b=n*(n+1)
        return self.gcd(a,b)