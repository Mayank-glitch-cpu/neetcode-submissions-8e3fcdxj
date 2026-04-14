class Solution:
    def isHappy(self, n: int) -> bool:
        seen= set()
        def detect(num):
            digits= [d for d in str(num)]
            happy=0
            for digit in digits:
                happy+= int(digit)**2
            if happy in seen:
                return False
            elif happy==1:
                return True
            else:
                seen.add(happy)
                return detect(happy)
        
        return detect(n)