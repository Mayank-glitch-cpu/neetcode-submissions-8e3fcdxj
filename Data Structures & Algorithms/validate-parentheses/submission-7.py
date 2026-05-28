class Solution:
    def isValid(self, s: str) -> bool:
        bmap= {'(':')', '[':']', '{':'}'}
        stack= []
        for bkt in s:
            if bkt in bmap: # its a opening bracket
                stack.append(bkt)
            else:
                if not stack or bkt !=  bmap[stack[-1]]:
                    return False
                stack.pop()
        return not stack