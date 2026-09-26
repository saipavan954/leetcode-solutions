class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7 :
            return True
        elif n<10:
            return False
        else:
            su=0
            while n>0:
                temp=n%10
                su +=temp**2
                n//=10
            return self.isHappy(su)
            
        