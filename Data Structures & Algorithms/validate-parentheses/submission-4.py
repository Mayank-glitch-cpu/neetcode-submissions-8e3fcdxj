class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map= {'[':']', '{':'}', '(':')'}
        stack=[]
        for bkt in s:
            if bkt in bracket_map: # a opening bracket
                stack.append(bkt) 
            else:
                if not stack or bkt != bracket_map[stack[-1]]:
                    return False
                stack.pop()
        return not stack