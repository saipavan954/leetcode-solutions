class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        s=min(nums)
        l=max(nums)
        for i in range(s,l+1):
            if i not in nums:
                res.append(i)
        return res