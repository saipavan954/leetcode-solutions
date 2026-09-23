class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        su=0
        n=len(nums)
        for i in range(1<<len(nums)):
            xor=0
            for j in range(n):
                if (i&(1<<j)):
                    xor^=nums[j]
            su+=xor
        return su