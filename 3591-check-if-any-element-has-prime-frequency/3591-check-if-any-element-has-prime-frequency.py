class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq={}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for count in freq.values():
            if count<2:
                continue
            is_prime =True
            for i in range(2,int(count**0.5)+1):
                if count%i==0:
                    is_prime = False
                    break
            if is_prime:
                return True
        return False

        