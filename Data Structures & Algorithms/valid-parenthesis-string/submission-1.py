class Solution:
    def checkValidString(self, s: str) -> bool:
        stack =[]
        buffer_indices = []
        for i, sym in enumerate(s):
            if sym == '(':
                stack.append(i)
            elif sym== '*':
                buffer_indices.append(i)
            else:
                if stack:
                    stack.pop()
                elif buffer_indices:
                    buffer_indices.pop()
                else:
                    return False
        
        while stack and buffer_indices:
            if stack[-1] < buffer_indices[-1]:
                stack.pop()
                buffer_indices.pop()
            else:
                break

        return True if not stack else False