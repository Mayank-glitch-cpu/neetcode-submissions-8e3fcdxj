class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=False
        if digits[-1] < 9:
            digits[-1]+=1
            return digits
        else:
            carry=True
            for i in range(len(digits)-2,-1,-1):
                digits[i+1]=0
                print('with carry True',digits)
                if digits[i]<9:
                    digits[i]+=1
                    carry= False
                    print('with carry false',digits)
                    break
        if carry:
            digits[0]=0
            digits.insert(0,1)
            return digits
        return digits