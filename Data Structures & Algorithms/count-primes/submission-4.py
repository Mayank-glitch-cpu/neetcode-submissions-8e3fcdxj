class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0

        res= [True]*n

        res[0]= res[1] = False

        for i in range(2,(int(n**(0.5))+1)):
            if res[i]:
                for j in range(i*i, n, i):
                    res[j]= False
        return sum(res)