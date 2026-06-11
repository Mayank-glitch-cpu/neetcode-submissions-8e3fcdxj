class Solution:
    def isHappy(self, n: int) -> bool:
        visit= set()
        def square_loop(n):
            compute = sum(int(digit)**2 for digit in str(n)) 
            if compute in visit:
                return False
            print(compute)
            visit.add(compute)
            if compute == 1:
                return True
            return square_loop(compute)

        return square_loop(n)