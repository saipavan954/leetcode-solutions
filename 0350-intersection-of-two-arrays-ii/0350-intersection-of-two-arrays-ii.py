class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        freq=Counter(nums2)
        for num in nums1:
            if freq[num]>0:
                ans.append(num)
                freq[num]-=1
        return ans
        