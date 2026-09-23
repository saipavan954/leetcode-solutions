class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            sum1=0
            while i>0:
                sum1 +=i%10
                i//=10
            res.append(sum1)
        return min(res)
           

        