class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        same=0
        count={}
        for i in range(len(nums)-1):
            a=nums[i]
            b=nums[i+1]
            if a==b:
                same +=1
            else:
                pair=(a,b)
                count[pair] = count.get(pair,0)+1
                pair=(b,a)
                count[pair] = count.get(pair,0)+1
                
        return same+max(count.values(),default=0)
        