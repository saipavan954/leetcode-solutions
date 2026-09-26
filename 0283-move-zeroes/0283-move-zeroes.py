class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        for i in nums:
            if i != 0:
                res.append(i)
        for i in range(len(nums)-len(res)):
            res.append(0)
        nums[:]=res
        return res
        