class Solution:
    def isValid(self, s: str) -> bool:
        mapping={'(':')','{':'}','[':']'}

        stack= []
        for char in s:
            if char in mapping: # its  an opening bracket
                stack.append(char)
            else:
                if not stack or char !=  mapping[stack[-1]]:
                    return False
                stack.pop()
        return not stack
    