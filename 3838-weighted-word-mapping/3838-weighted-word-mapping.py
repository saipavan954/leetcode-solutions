class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=[]
        for word in words:
            s=0
            for i in word:
                s+=weights[ord(i)-ord('a')]
            remainder=s%26
            ans.append(chr(ord('z')-remainder))
        return "".join(ans)
        