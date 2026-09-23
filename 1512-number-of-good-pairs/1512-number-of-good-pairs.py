class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count =  0
        len_nums = len(nums)

        for i in range(len_nums-1):
            for j in range(i+1, len_nums):
                if nums[i] == nums[j]: count +=1
        return count