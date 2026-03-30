class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out=[]
        curr=[]
        def backtrack(i):
            digit_map= {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
            if i >=len(digits):
                out.append(''.join(curr))
                print(out)
                return 

            for char in digit_map[int(digits[i])]:
                curr.append(char)
                print(curr)
                backtrack(i+1)
                curr.pop()
        if digits:
            backtrack(0)
        return out


