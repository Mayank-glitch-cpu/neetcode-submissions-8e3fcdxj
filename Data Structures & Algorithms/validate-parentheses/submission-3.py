class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map= {"(":")", "[":"]", "{":"}"}

        for bracket in s:
            if bracket in b_map:
                stack.append(bracket) # its a openinig bracket
            else:
                if not stack or bracket != b_map[stack[-1]]: # check there is nothing opened like this before
                    return False
                stack.pop()
        return not stack