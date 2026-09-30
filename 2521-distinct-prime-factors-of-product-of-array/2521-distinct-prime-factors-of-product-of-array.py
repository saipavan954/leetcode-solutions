class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        prime =set()
        for num in nums:
            i=2
            while i*i<=num:
                if num%i==0:
                    prime.add(i)
                    while num%i==0:
                        num//=i
                i+=1
            if num>1:
                prime.add(num)
        return len(prime)        