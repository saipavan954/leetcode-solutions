class Solution:
    def countBits(self, n: int) -> list[int]:
        res=[]
        for i in range(n+1):
            cnt=0
            x=1
            while(x<=i):
                if ((x&i)>0):
                    cnt+=1
                x=x<<1
            res.append(cnt)
        return res
                

        