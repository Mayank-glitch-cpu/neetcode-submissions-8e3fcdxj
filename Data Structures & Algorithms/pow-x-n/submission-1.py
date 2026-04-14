class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        factor= x
        if n>0:
            while n>1:
                x*=factor
                n-=1
            return x
        else:
            while n<-1:
                x*=factor
                n+=1
            return 1/x
