class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if nums.count(i)==2:
                nums.remove(i)
                res.append(i)
        return res

        