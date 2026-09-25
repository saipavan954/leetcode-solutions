class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sub1=[]
        for i in range(1<<n):
            sub2=[]
            for j in range(n):
                if i&(1<<j):
                    sub2.append(nums[j])
            sub1.append(sub2)

        return sub1