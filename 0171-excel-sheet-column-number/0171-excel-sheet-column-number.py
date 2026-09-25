class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        n=len(columnTitle)-1
        for i in columnTitle:
            ans=ans+(ord(i)-64)*26**n
            n-=1
        return ans