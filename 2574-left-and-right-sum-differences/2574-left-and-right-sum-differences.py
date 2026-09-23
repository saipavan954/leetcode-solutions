class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        left_sum=0
        total=sum(nums)
        for i in range(len(nums)):
            res.append(abs(2*left_sum - total + nums[i]))
            left_sum+=nums[i]
        return res

            
        