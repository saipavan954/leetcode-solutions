from collections import Counter 
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq=Counter(nums)
        ans=[]
        while freq:
            
            for x in sorted(freq):
                ans.append(x)
                freq[x]-=1
                if freq[x] == 0:
                    del freq[x]
        return ans
        
        
        